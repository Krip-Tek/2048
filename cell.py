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

