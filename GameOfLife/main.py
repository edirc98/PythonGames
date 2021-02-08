#Conway's Game Of Life - Main 
from clases.gameClass import Board
import pygame
import time

#Colors
BG_COLOR = (10,10,10)
ALIVE_COLOR = (63,255,82)
DEAD_COLOR = (128,128,128)
PAUSED_COLOR = (255,255,128)

pygame.init()
#Screen width and heigh
width,heigh = 800,800
screen = pygame.display.set_mode((heigh,width))
screen.fill(BG_COLOR)

game = Board(30,30)
game.CellWidthHeigh(width,heigh)




def main():
    #Execution boolean
    ExitGame = False
    PauseExecution = False
    #main execution loop
    while not ExitGame:
        #Screen refill
        if not PauseExecution:
            screen.fill(BG_COLOR)
        game.set_newGamestate(game.get_GameState())

        #EVENTS CONTROL
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                ExitGame = True

            if event.type == pygame.KEYDOWN:
                PauseExecution = not PauseExecution

        #MouseDetection
        mouseClick = pygame.mouse.get_pressed()

        #Set a live cell(Left Click)
        if mouseClick[0] == 1: 
            posX,posY = pygame.mouse.get_pos()
            cellX,cellY = game.mousePosToCell(posX,posY)
            game.ChangeCellStatus(cellX,cellY,1)

        #Kill a cell(Right Click)
        elif mouseClick[2] == 1:
            posX,posY = pygame.mouse.get_pos()
            cellX,cellY = game.mousePosToCell(posX,posY)
            game.ChangeCellStatus(cellX,cellY,0)
        
        for x in range(0,game.get_numCellX()):
            for y in range(0,game.get_numCellY()):

                if not PauseExecution:
                    #Neighbor cells
                    n_neigh = game.num_Neigh(x,y)

                    #Game Rules
                    #(1)A dead Cell revive with 3 alive neigbor cells
                    if game.get_CellGameState(x,y) == 0 and n_neigh == 3:
                        game.ChangeCellStatus(x,y,1)
                    
                    #(2)An Alive cell, dies with less than 2 neighbors or more than 3
                    elif game.get_CellGameState(x,y) == 1 and (n_neigh < 2 or n_neigh > 3):
                        game.ChangeCellStatus(x,y,0)


                #Draw board
                poly = game.createPoly(x,y)
                if game.get_CellnewGameState(x,y) == 0:
                    pygame.draw.polygon(screen,DEAD_COLOR,poly,2)

                elif PauseExecution and game.get_CellnewGameState(x,y) == 1:
                    pygame.draw.polygon(screen,PAUSED_COLOR,poly,0)

                elif PauseExecution and game.get_CellnewGameState(x,y) == 0:
                    pygame.draw.polygon(screen,DEAD_COLOR,poly,0)
                      
                else:
                    pygame.draw.polygon(screen,ALIVE_COLOR,poly,0)  

        game.set_GameState(game.get_newGameState())
        pygame.display.flip()
        time.sleep(0.1)

main()