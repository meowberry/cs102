'''
Custom process pool
'''

import psutil
import time
import queue
import multiprocessing
from psutil import Process as psProcess
import math
import numpy as np
import warnings


def worker(function, data_chunk, return_values):
    result = function(data_chunk)
    return_values[data_chunk] = result


class ProcessPool:
    def __init__(self, min_workers=2, max_workers=10, mem_usage='1Gb'):
        self.min_workers = min_workers
        self.max_workers = max_workers
        self.mem_usage = int(float(mem_usage[:-2]) * 1024 * 1024)
        self.workers = 0
        self.processes = []
        manager = multiprocessing.Manager()
        self.return_values = manager.dict()
        print('Доступно память:', self.mem_usage, '(в Кбайт)')

    def map(self, function, big_data):
        self.queue = queue.Queue()
        for data_chunck in big_data:
            self.queue.put(data_chunck)
        print('В очереди:', self.queue.qsize(), ' задач.')
        self.pool(function)
        return self.return_values

    def pool(self, function):
        if not self.queue.empty():
            p = multiprocessing.Process(target=worker, args=(
                function, self.queue.get(), self.return_values))
            p.start()
            max_worker_mem = self.monitor(p.pid)
            self.max_workers = min(self.max_workers, math.floor(
                self.mem_usage / max_worker_mem))
            if self.max_workers < self.min_workers:
                raise MemoryError(
                    "Извините, у вас недостаточно памяти для создания минимального количества потоков")
                print('Вы можете максимально создать: ',
                      self.max_workers, ' потоков.')
            while not self.queue.empty() or self.workers > 0:
                for process in self.processes:
                    if not process.is_alive():
                        self.workers -= 1
                        self.processes.remove(process)
                if self.workers < self.max_workers and not self.queue.empty():
                    self.create_worker(function, self.queue.get_nowait())

            print('done!.....')
            self.info_process.kill()

    def create_worker(self, function, data_chunk):
        self.workers += 1
        p = multiprocessing.Process(target=worker, args=(
            function, data_chunk, self.return_values))
        p.start()
        self.processes.append(p)

    def monitor(self, pid):
        max_mem = 0
        max_cpu = 0.0
        cur_process = psProcess(pid)
        while cur_process.is_running():
            try:
                mem = cur_process.memory_info().rss
                if mem > max_mem:
                    max_mem = mem
                cpu = cur_process.cpu_percent(interval=None)
                if cpu > max_cpu:
                    max_cpu = cpu
            except:
                pass
        print('Самый высокий пик: ', int(max_mem / 1024),
              'кбайт. Загружается процессор: ', float(max_cpu))
        return int(max_mem / 1024)

    def info(self):
        info_process = multiprocessing.Process(target=self.show_info)
        info_process.start()
        self.info_process = info_process

    def show_info(self):
        while True:
            number_of_processes = 0
            cpu = 0
            using_men = 0
            for process in psutil.process_iter():
                if process.name() == 'python.exe':
                    using_men += process.memory_info().rss
                    cpu += process.cpu_percent()
                    number_of_processes += 1
            print('Количество процессов: {0}, используется {1} Кбайт памяти, cpu: {2}'.format(
                number_of_processes, using_men / 1024, cpu))
            time.sleep(0.5)


def heavy_computation(data_chunk):
    h = np.dot(np.fromstring(data_chunk), np.fromstring(data_chunk))
    time.sleep(3)
    return h


if __name__ == '__main__':
    warnings.simplefilter("ignore", DeprecationWarning)
    big_data = [np.random.random((40, 40, 40)).tostring() for i in range(14)]
    pool = ProcessPool()
    results = pool.map(heavy_computation, big_data)
    print(len(results))
