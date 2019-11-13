import pathlib
import random
import copy

from typing import List, Optional, Tuple

Cell = Tuple[int, int]
Cells = List[int]
Grid = List[Cells]


class GameOfLife:

    def __init__(
            self,
            size: Tuple[int, int],
            randomize: bool = True,
            max_generations: Optional[float] = float('inf')
    ) -> None:
        # Размер клеточного поля
        self.cols, self.rows = size
        # Предыдущее поколение клеток (тут не нужно)
        self.prev_generation = self.create_grid()
        # Текущее поколение клеток
        self.curr_generation = self.create_grid(randomize=randomize)
        # Максимальное число поколений
        self.max_generations = max_generations
        # Текущее число поколений
        self.generations = 1

    def create_grid(self, randomize: bool = False) -> Grid:
        grid = [[0 for _ in range(self.rows)] for _ in range(self.cols)]
        if randomize:
            for i in range(self.cols):
                for j in range(self.rows):
                    grid[i][j] = random.randint(0, 1)
        return grid

    def get_neighbours(self, cell: Cell) -> Cells:
        neighbours = []
        for i in range(-1, 2):
            for j in range(-1, 2):
                if 0 <= cell[0] + i < self.cols and 0 <= cell[1] + j < self.rows and (i, j) != (0, 0):
                    neighbours.append(
                        self.curr_generation[cell[0] + i][cell[1] + j])
        return neighbours

    def get_next_generation(self) -> Grid:
        new_grid = self.create_grid(False)
        for i in range(self.cols):
            for j in range(self.rows):
                if (self.curr_generation[i][j] == 0) and sum(self.get_neighbours([i, j])) == 3:
                    new_grid[i][j] = 1
                elif (self.curr_generation[i][j] == 1) and (2 <= sum(self.get_neighbours([i, j])) <= 3):
                    new_grid[i][j] = 1

        return new_grid

    def step(self) -> None:
        """
        Выполнить один шаг игры.
        """
        self.prev_generation = copy.deepcopy(self.curr_generation)
        self.curr_generation = self.get_next_generation()
        self.generations += 1
        pass

    @property
    def is_max_generations_exceeded(self) -> bool:
        """
        Не превысило ли текущее число поколений максимально допустимое.
        """
        if self.generations == self.max_generations:
            return True
        else:
            return False

    @property
    def is_changing(self) -> bool:
        """
        Изменилось ли состояние клеток с предыдущего шага.
        """
        if self.prev_generation != self.curr_generation:
            return True
        else:
            return False

    @staticmethod
    def from_file(filename: pathlib.Path) -> 'GameOfLife':
        """
        Прочитать состояние клеток из указанного файла.
        """
        with open(filename) as file:
            grid = [[int(a) for a in list(row)] for row in file.readlines()]
        rows, cols = len(grid), len(grid[0])

        game = GameOfLife((rows, cols))
        game.prev_generation = GameOfLife.create_grid(game)
        game.curr_generation = grid
        return game

    def save(self, filename: pathlib.Path) -> None:
        """
        Сохранить текущее состояние клеток в указанный файл.
        """
        with open(filename) as file:
            for i in range(self.rows):
                for j in range(self.cols):
                    file.write(str(self.curr_generation[i][j]))
                file.write('\n')
        file.close()
