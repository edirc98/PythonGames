import pygame
class Player:
    __PlayersColor = (255,255,255)
    def __init__(self,widht,heigh,x,y,speed):
        self.__rect = pygame.Rect(x,y,widht,heigh)
        self.__speed = speed
        self.__color = self.__PlayersColor

    #Getters & Setters

    #Functions
    def movePlayer(self):
        pass
    def drawPlayer(self):
        pass