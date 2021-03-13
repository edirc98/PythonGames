import pygame
import random
class Ball:
    __BallColor = (255,255,255)
    def __init__(self,width,height,x,y,speed,screen):
        self.__rect = pygame.Rect(x,y,width,height)
        self.__speed = [speed,speed] #Speed [0] is X speed, and speed [1] is Y speed
        self.__color = self.__BallColor
        self.__screen = screen


    #Getters & Setters
    def get_rect(self):
        return self.__rect
    #Functions
    def move(self):
        self.__rect.x += self.__speed[0]
        self.__rect.y += self.__speed[1]
    def bouncy(self):
        if self.__rect.top <= 0 or self.__rect.bottom >= self.__screen.get_height():
            self.__speed[1] *= -1
        
    def playerCollision(self):
        self.__speed[0] *= -1
    def UpdateScore(self,player,opponent):
        if self.__rect.left <=0:
            opponent.updateScore()
            self.ballRestart()
        if self.__rect.right >= self.__screen.get_width():
            player.updateScore()
            self.ballRestart()

    def ballRestart(self):
        self.__rect.center = (self.__screen.get_width()/2,self.__screen.get_height()/2)
        self.__speed[0] *= random.choice((1,-1))
        self.__speed[1] *= random.choice((1,-1))

    def draw(self):
        pygame.draw.ellipse(self.__screen,self.__color,self.__rect)