import pygame

pygame.init()


screen = pygame.display.set_mode((800, 600))  # (ширина, высота)

while True:

    for events in pygame.event.get():
        if events.type == pygame.QUIT:
            exit()

    pygame.display.update()
