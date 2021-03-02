import pygame
class Ball:
    __BallColor = (255,255,255)
    def __init__(self,x,y,widh,heigh,speed):
        self.__rect = pygame.Rect(x,y,widh,heigh)
        self.__speed = speed
        self.__color = self.__BallColor


    #Getters & Setters

    #Functions
    def moveBall(self):
        pass
    def drawBall(self):
        pass