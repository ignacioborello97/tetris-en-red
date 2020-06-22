import pygame
from client.components.entities.colors.colores import *

class Board:
    def __init__(self,x,y,block_size):
        self.x = x
        self.y = y
        self.block_size = block_size
        self.grid = [[black for _ in range(10)] for _ in range(20)]

    def draw(self,surface):
        pygame.draw.rect(surface,bright_yellow,(self.x,self.y,self.block_size*10,self.block_size*20),int(min(self.block_size/2,6)))
        for i in range(len(self.grid)):
            for j in range(len(self.grid[i])):
                pygame.draw.rect(surface,self.grid[i][j],(self.x+j*self.block_size,self.y+i*self.block_size,self.block_size,self.block_size),0)
    
    def update(self,matriz_server):
        for i in range(len(matriz_server)):
            for j in range(len(matriz_server[i])):
                for k in range(len(matriz_server[i][j])):
                    if matriz_server[i][j][k] == '.':
                        self.grid[i][j] = black
                    if matriz_server[i][j][k] == 'S':
                        self.grid[i][j] = red
                    if matriz_server[i][j][k] == 'T':
                        self.grid[i][j] = fucsia
                    if matriz_server[i][j][k] == 'J':
                        self.grid[i][j] = green
                    if matriz_server[i][j][k] == 'Z':
                        self.grid[i][j] = light_blue
                    if matriz_server[i][j][k] == 'O':
                        self.grid[i][j] = yellow
                    if matriz_server[i][j][k] == 'I':
                        self.grid[i][j] = purple
