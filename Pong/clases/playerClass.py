import pygame

class Player:
    __PlayersColor = (255,255,255)
    def __init__(self,widht,heigh,x,y,speed,screen):
        self.__rect = pygame.rect.Rect(x,y,widht,heigh)
        self.__speed = speed
        self.__color = self.__PlayersColor
        self.__screen = screen

    #Getters & Setters

    #Functions
    def movePlayer(self):
        pass
    def draw(self):
        pygame.draw.rect(self.__screen,self.__color,self.__rect)