import pygame
from pygame.sprite import Sprite


class Cell(Sprite):
    def __init__(self, screen, x_pos=5, y_pos=5, n_cell=2, ):
        super().__init__()
        self.image = pygame.image.load("cell_2.bmp")
        self.rect = self.image.get_rect()

        self.rect.x = x_pos
        self.rect.y = y_pos

        self.num_cell = n_cell

    def move_cell(self, side, step_len):
        if side == "left":
            self.rect.x -= step_len
        elif side == "right":
            self.rect.x += step_len
        elif side == "up":
            self.rect.y -= step_len
        elif side == "down":
            self.rect.y += step_len

    def get_pos(self):
        return self.rect.x, self.rect.y
