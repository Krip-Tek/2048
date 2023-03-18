import pygame

from pygame.sprite import Group
from field import Field
pygame.init()

WIGTH = 450
HEIGHT = 450


screen = pygame.display.set_mode((WIGTH, HEIGHT))  # (ширина, высота)
screen.fill("#7179C2")

field_cells = Group()


def field_cell_init():
    for i in range(0, round(WIGTH)-51, 110):
        for j in range(0, round(HEIGHT) - 51, 110):
            f = Field(screen, i, j)
            field_cells.add(f)


field_cell_init()
field_cells.draw(screen)

while True:

    for events in pygame.event.get():
        if events.type == pygame.QUIT:
            exit()

    pygame.display.update()
