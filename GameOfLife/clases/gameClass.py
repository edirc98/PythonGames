#Conway's Game Of Life - Class Board
#Stores gameState data, and all functions related to the matrix positions
import numpy as np

class Board:
    __dimW = None
    __dimH = None
    #Constructor
    def __init__(self,x,y):
        self.__GameState = np.zeros((x,y))
        self.__newGameState = self.__GameState
        self.__ncX = x
        self.__ncY = y


    #Num cells
    def get_numCellX(self):
        return self.__ncX
    def get_numCellY(self):
        return self.__ncY
    
    #Dimensions Width&Heigh
    def get_dimW(self):
        return self.__dimW  
    def get_dimH(self):
        return self.__dimH    

    #GameState
    def get_CellGameState(self,x,y):
        return self.__GameState[x,y]
    def get_GameState(self):
        return self.__GameState
    def set_GameState(self,newGameState):
        self.__GameState = np.copy(newGameState)

    #newGameState
    def get_CellnewGameState(self,x,y):
        return self.__newGameState[x,y]
    def get_newGameState(self):
        return self.__newGameState
    def set_newGamestate(self,newGameState):
        self.__newGameState = np.copy(newGameState)

    #Functions 
    def CellWidthHeigh(self,screenWidth, screenHeigh):
        self.__dimW = screenWidth / self.__ncX
        self.__dimH = screenHeigh / self.__ncY  

    #Changes are aplied on newGameState by default, status is 0 or 1
    def ChangeCellStatus(self,x,y,status):
        self.__newGameState[x,y] = status

    def createPoly(self,x,y):
        poly = [((x)  * self.__dimW,  y    * self.__dimH),
               ((x+1) * self.__dimW,  y    * self.__dimH),
               ((x+1) * self.__dimW, (y+1) * self.__dimH),
               ((x)   * self.__dimW, (y+1) * self.__dimH)]
        return poly

    def mousePosToCell(self,posX,posY):
        cellX,CellY = int(np.floor(posX / self.__dimW)), int(np.floor(posY/self.__dimW))
        return cellX,CellY

    def num_Neigh(self,x,y):
       return self.__GameState[(x-1) % self.__ncX,(y-1) % self.__ncY] + self.__GameState[(x)   % self.__ncX,(y-1) % self.__ncY] + \
              self.__GameState[(x+1) % self.__ncX,(y-1) % self.__ncY] + self.__GameState[(x-1) % self.__ncX,(y)   % self.__ncY] + \
              self.__GameState[(x+1) % self.__ncX,(y)   % self.__ncY] + self.__GameState[(x-1) % self.__ncX,(y+1) % self.__ncY] + \
              self.__GameState[(x)   % self.__ncX,(y+1) % self.__ncY] + self.__GameState[(x+1) % self.__ncX,(y+1) % self.__ncY]