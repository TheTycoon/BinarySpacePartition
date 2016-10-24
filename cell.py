'''
This was a direct copy over from the cellular automata cell class
Still needs to be revised to work with nodes
'''

import pygame
import settings
from random import randint


class Cell:
    def __init__(self, column, row, state):
        self.column = column
        self.row = row
        #self.neighborhood = []
        self.rect = pygame.Rect(self.column * settings.TILESIZE, self.row * settings.TILESIZE,
                                settings.TILESIZE, settings.TILESIZE)
        self.state = True
        self.temp_state = self.state

'''
    def set_neighborhood(self, grid):
        self.neighborhood.append(grid.get_cell(self.column - 1, self.row - 1))
        self.neighborhood.append(grid.get_cell(self.column, self.row - 1))
        self.neighborhood.append(grid.get_cell(self.column + 1, self.row - 1))
        self.neighborhood.append(grid.get_cell(self.column - 1, self.row))
        self.neighborhood.append(grid.get_cell(self.column + 1, self.row))
        self.neighborhood.append(grid.get_cell(self.column - 1, self.row + 1))
        self.neighborhood.append(grid.get_cell(self.column, self.row + 1))
        self.neighborhood.append(grid.get_cell(self.column + 1, self.row + 1))

    def check_neighborhood(self):
        living_cells = 0
        for i in range(len(self.neighborhood)):
            living_cells += self.neighborhood[i].state
        return living_cells
'''


class Map:
    def __init__(self):
        self.grid = self.set_grid()
        #self.create_neighborhoods()

    def set_grid(self):
        grid = []
        for column in range(settings.COLUMNS):
            grid.append([])
            for row in range(settings.ROWS):
                grid[column].append(Cell(column, row, randint(0, 100)))
        return grid