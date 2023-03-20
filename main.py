import random

import pygame

from pygame.sprite import Group
from field import Field
from cell import Cell


pygame.init()

WIDTH = 425
HEIGHT = 425


screen = pygame.display.set_mode((WIDTH, HEIGHT))  # (ширина, высота)
pygame.display.set_caption("2048")
icon = pygame.image.load("2048.png")
pygame.display.set_icon(icon)
screen.fill("#7179C2")

field_cells = Group()
cells = Group()


def cell_spawn(field_cells):

    lists = field_cells.sprites()
    random.shuffle(lists)
    for f_cells in lists:
        if not f_cells.filling:   #* не занято?
            cell = Cell(screen, f_cells.rect.x, f_cells.rect.y, 2)
            cells.add(cell)
            print("Пустой", f_cells.rect.x, f_cells.rect.y)
            f_cells.filling = True
            break


def field_cell_init():
    for i in range(0, round(WIDTH)-26, 105):
        for j in range(0, round(HEIGHT) - 26, 105):
            f = Field(screen, i, j)
            field_cells.add(f)


field_cell_init()
field_cells.draw(screen)

while True:

    for events in pygame.event.get():
        if events.type == pygame.QUIT:
            exit()
        if events.type == pygame.KEYDOWN:
            if events.key == pygame.K_SPACE:
                cell_spawn(field_cells)

    cells.draw(screen)

    pygame.display.update()
