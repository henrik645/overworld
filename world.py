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
                self.map[y].append(Tile(TileType.path))