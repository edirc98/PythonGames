import pygame
class Ball:
    __BallColor = (255,255,255)
    def __init__(self,widh,heigh,x,y,speed,screen):
        self.__rect = pygame.Rect(x,y,widh,heigh)
        self.__speed = [speed,speed] #Speed [1] is X speed, and speed [2] is Y speed
        self.__color = self.__BallColor
        self.__screen = screen


    #Getters & Setters

    #Functions
    def move(self):
        pass
    def draw(self):
        pygame.draw.ellipse(self.__screen,self.__color,self.__rect)