import pygame
from settings import *
from map import *

pygame.init()
sc = pygame.display.set_mode((WIDTH,HEIGHT))
clock = pygame.time.Clock()

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            exit()
    grid(sc,GRID_COLOR)

    pygame.display.flip()
    clock.tick(FPS)
