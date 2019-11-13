import pygame
from pygame.locals import *

from life import GameOfLife
from ui import UI


class GUI(UI):

    def __init__(self, life: GameOfLife, cell_size: int = 10, speed: int = 5) -> None:
        super().__init__(life)
        self.cell_size = cell_size
        self.speed = speed
        self.width = self.life.rows * cell_size
        self.height = self.life.cols * cell_size
        self.screen = pygame.display.set_mode((self.width, self.height))

    def draw_lines(self) -> None:
        """ Отрисовать сетку """
        for x in range(0, self.width, self.cell_size):
            pygame.draw.line(self.screen, pygame.Color('black'),
                             (x, 0), (x, self.height))
        for y in range(0, self.height, self.cell_size):
            pygame.draw.line(self.screen, pygame.Color('black'),
                             (0, y), (self.width, y))

    def draw_grid(self) -> None:
        """
        Отрисовка списка клеток с закрашиванием их в соответствующе цвета.
        """
        for i in range(self.life.rows):
            for j in range(self.life.cols):
                if self.life.curr_generation[i][j] == 1:
                    color = pygame.Color('green')
                else:
                    color = pygame.Color('white')
                pygame.draw.rect(self.screen, color, (
                    i * self.cell_size + 1, j * self.cell_size + 1, self.cell_size - 1, self.cell_size - 1))
        pass

    def run(self) -> None:
        """ Запустить игру """
        pygame.init()
        clock = pygame.time.Clock()
        pygame.display.set_caption('Game of Life')
        self.screen.fill(pygame.Color('white'))

        paused = False
        running = True
        while running:
            for i in pygame.event.get():
                if i.type == QUIT:
                    running = False
                if i.type == KEYDOWN and i.key == K_SPACE:
                    paused = not paused
                if i.type == MOUSEBUTTONDOWN:
                    if paused:
                        click_pos = pygame.mouse.get_pos()
                        x = click_pos[0] // self.cell_size
                        y = click_pos[1] // self.cell_size
                        self.life.curr_generation[x][y] = -1 * (self.life.curr_generation[x][y] - 1)
            self.draw_lines()
            self.draw_grid()
            if paused:
                pass
            else:
                if not self.life.is_max_generations_exceeded:
                    self.life.step()
            pygame.display.flip()
            clock.tick(self.speed)
        pygame.quit()


if __name__ == '__main__':
    life = GameOfLife((24, 24), max_generations=500)
    gui = GUI(life)
    gui.run()
