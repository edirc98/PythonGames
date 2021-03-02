import pygame

class Player:
    __PlayersColor = (255,255,255)
    def __init__(self,widht,heigh,x,y,screen):
        self.__rect = pygame.rect.Rect(x,y,widht,heigh)
        self.__color = self.__PlayersColor
        self.__screen = screen


    #Functions
    def move(self,speed):
        self.__rect.y += speed
    def draw(self):
        pygame.draw.rect(self.__screen,self.__color,self.__rect)