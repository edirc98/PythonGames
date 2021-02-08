#Conway's Game Of Life - Main 
from clases.gameClass import Board
import pygame



pygame.init()
#Screen width and heigh
width,heigh = 800,800
screen = pygame.display.set_mode((heigh,width))


game = Board(30,30)
game.CellWidthHeigh(width,heigh)




def main():
    #Execution boolean
    ExitGame = False

    #main execution loop
    while not ExitGame:

        
        for x in range(0,game.get_numCellX()):
            for y in range(0,game.get_numCellY()):




                #Draw board
                poly = game.createPoly(x,y)
                pygame.draw.polygon(screen,(255,255,255),poly,1)   


        pygame.display.flip()

main()