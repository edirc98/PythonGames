import pygame

class Player:
    __PlayersColor = (255,255,255)
    def __init__(self,widht,heigh,x,y,speed,screen):
        self.__rect = pygame.rect.Rect(x,y,widht,heigh)
        self.__color = self.__PlayersColor
        self.__screen = screen
        self.__speed = speed
        self.__score = 0
        self.__font = pygame.font.Font("freesansbold.ttf",25)

    #Getters & Setters
    def getScore(self):
        return self.__score
    #Functions
    def move(self,dir):
        self.__rect.y += (self.__speed*dir)
    def collisions(self,ball):
        if self.__rect.colliderect(ball.get_rect()):
            ball.playerCollision()
    def updateScore(self):
        self.__score += 1
    def updateText(self,offset):
        player_text = self.__font.render(f"{self.__score}",False, self.__color)
        self.__screen.blit(player_text,(((self.__screen.get_width()/2) + offset),abs(offset)))
        

    def draw(self):
        pygame.draw.rect(self.__screen,self.__color,self.__rect)