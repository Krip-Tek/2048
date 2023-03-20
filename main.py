import random

import pygame

from pygame.sprite import Group
from field import Field
from cell import Cell


pygame.init()

WIDTH = 425
HEIGHT = 425

2
screen = pygame.display.set_mode((WIDTH, HEIGHT))  # (ширина, высота)
pygame.display.set_caption("2048")
icon = pygame.image.load("2048.png")
pygame.display.set_icon(icon)
screen.fill("#7179C2")

field_cells = Group()
cells = Group()

cell = Cell(screen, random.randrange(5, round(WIDTH)-26, 105), random.randrange(5, round(HEIGHT) - 26, 105), 2)
cells.add(cell)


def cell_spawn(field_cells):
    lists = field_cells.sprites()
    random.shuffle(lists)
    for f_cells in lists:
        if not f_cells.filling:   #* не занято?
            cell = Cell(screen, f_cells.rect.x, f_cells.rect.y, 2)
            cells.add(cell)
            f_cells.filling = True
            break


def field_cell_init():
    for i in range(0, round(WIDTH)-26, 105):
        for j in range(0, round(HEIGHT) - 26, 105):
            f = Field(screen, i, j)
            field_cells.add(f)


def control():
    #* Функция управления игрой.
    #* Сдержит алгоритм соединения либо движения ячеек


    pass


field_cell_init()
field_cells.draw(screen)

while True:

    for events in pygame.event.get():
        if events.type == pygame.QUIT:
            exit()
        if events.type == pygame.KEYDOWN:
            if events.key == pygame.K_w:
                cell_spawn(field_cells)
                cell.move_cell("up")
            elif events.key == pygame.K_s:
                cell_spawn(field_cells)
                cell.move_cell("down")
            elif events.key == pygame.K_a:
                cell_spawn(field_cells)
                cell.move_cell("left")
            elif events.key == pygame.K_d:
                cell_spawn(field_cells)
                cell.move_cell("right")

    cells.draw(screen)

    pygame.display.update()
