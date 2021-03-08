import pygame
from settings import *

def grid(sc,color):
    sc.fill(BLACK) 
    x = 0
    while x < WIDTH:
        pygame.draw.line(sc,color,(x,0),(x,HEIGHT))
        x+=CELL_LEN
    pygame.draw.line(sc,color,(WIDTH-1,0),(WIDTH-1,HEIGHT-1))
    y = 0
    while y < HEIGHT:
        pygame.draw.line(sc,color,(0,y),(WIDTH,y))
        y+=CELL_LEN
    pygame.draw.line(sc,color,(0,HEIGHT-1),(WIDTH-1,HEIGHT-1))
    pygame.draw.rect(sc, color, pygame.Rect(CELL_LEN, CELL_LEN, CELL_LEN, CELL_LEN)) 
    pygame.display.flip() 
    

    