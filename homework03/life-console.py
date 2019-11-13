import curses
import time

from life import GameOfLife
from ui import UI


class Console(UI):

    def __init__(self, life: GameOfLife) -> None:
        super().__init__(life)

    def draw_borders(self, screen) -> None:
        screen.border(0)

    def draw_grid(self, screen) -> None:
        for i in range(self.life.cols):
            for j in range(self.life.rows):
                try:
                    if self.life.curr_generation[i][j]:
                        screen.addch(i + 1, j + 1, '*')
                    # else:
                    #     screen.addch(i + 1, j + 1, ' ')
                except:
                    pass

    def run(self) -> None:
        screen = curses.initscr()
        paused = False
        while not self.life.is_max_generations_exceeded and self.life.is_changing:
            screen.clear()
            self.draw_borders(screen)
            self.draw_grid(screen)
            self.life.step()
            screen.refresh()
            time.sleep(1 / 60)
        curses.endwin()


if __name__ == '__main__':
    life = GameOfLife((30, 80), max_generations=500)
    ui = Console(life)
    ui.run()
