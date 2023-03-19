import pygame
from pygame.sprite import Sprite


class Field(Sprite):

    def __init__(self, screen,  x_pos, y_pos,):
        super().__init__()
        self.image = pygame.image.load("field_cell.bmp")
        self.rect = self.image.get_rect()
        self.rect.x = 5+x_pos
        self.rect.y = 5+y_pos
        self.filling = False




