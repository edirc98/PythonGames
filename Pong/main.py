import pygame
import time
import sys

#Colors
BG_COLOR = pygame.Color(40,40,40)

pygame.init()
clock = pygame.time.Clock()
#Screen width and heigh
width,heigh = 1280,720
screen = pygame.display.set_mode((width,heigh))
pygame.display.set_caption("Pong")
screen.fill(BG_COLOR)


def main():
    #Execution boolean
    ExitGame = False
    #main execution loop
    while not ExitGame:
        #Screen refill
        screen.fill(BG_COLOR)

        #EVENTS CONTROL
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                ExitGame = True

        #Window update
        pygame.display.flip()
        clock.tick(60)




main()