import pygame

class Player:
    __PlayersColor = (255,255,255)
    def __init__(self,widht,heigh,x,y,speed,screen):
        self.__rect = pygame.rect.Rect(x,y,widht,heigh)
        self.__color = self.__PlayersColor
        self.__screen = screen
        self.__speed = speed


    #Functions
    def move(self,dir):
        self.__rect.y += (self.__speed*dir)
    def collisions(self,ball):
        if self.__rect.colliderect(ball.get_rect()):
            ball.playerCollision()

    def draw(self):
        pygame.draw.rect(self.__screen,self.__color,self.__rect)