import pygame
import time
from clases.playerClass import Player
from clases.ballClass import Ball

#Colors
BG_COLOR = pygame.Color(40,40,40)

pygame.init()
clock = pygame.time.Clock()
#Screen width and heigh
screen_width,screen_heigh = 1280,720
screen = pygame.display.set_mode((screen_width,screen_heigh))
pygame.display.set_caption("Pong")
screen.fill(BG_COLOR)

#Player instances
player = Player(10,80,20,(screen_heigh/2)-40,4,screen)
opponent = Player(10,80,screen_width - 20,(screen_heigh/2)-40,4,screen)
ball = Ball(20,20,(screen_width/2) - 10,(screen_heigh/2) - 10,7,screen)
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


        #Draw Elements
        player.draw()
        opponent.draw()
        ball.draw()
        #Window update
        pygame.display.flip()
        clock.tick(60)




main()