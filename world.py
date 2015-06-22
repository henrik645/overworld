"""
This file defines all functions associated with world generation and viewing
"""

from tile import Tile
from tile import TileType

class Level:
    def __init__(self, width, height):
        self.width = width
        self.height = height
        self.map = []
        
        for y in range(0, height):
            self.map.append([])
            for x in range(0, width):
                self.map[y].append(Tile(TileType.void))
        self.draw_room(5, 5, 15, 15)

    def draw_room(self, x0, y0, x1, y1): #Draws a rectangular room
        if x0 > x1:
            x0, x1 = x1, x0
        if y0 > y1:
            x0, y1 = y1, y0

        for x in range(x0, x1):
            for y in range(y0, y1):
                self.plot_tile(x, y, Tile(TileType.path))

        self.plot_line_horizontal(y0, x0, x1, Tile(TileType.wall)) #Plots upper horizontal wall
        self.plot_line_horizontal(y1, x0, x1, Tile(TileType.wall)) #Plots lower horizontal wall
        self.plot_line_vertical(x0, y0, y1, Tile(TileType.wall)) #Plots left-most vertical wall
        self.plot_line_vertical(x1, y0, y1, Tile(TileType.wall)) #Plots right-most vertical wall

    def plot_tile(self, x, y, tile):
        self.map[y][x] = tile 
    
    def plot_line_vertical(self, x, y0, y1, tile):
        for y in range(y0, y1 + 1):
            self.plot_tile(x, y, tile)

    def plot_line_horizontal(self, y, x0, x1, tile):
        for x in range(x0, x1 + 1):
            self.plot_tile(x, y, tile)
