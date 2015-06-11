"""
This file defines a class named Tile and functions associated with it.
The Tile class is used for representing tiles in the game world.
"""

class TileType:
    path = 1
    wall = 2
    player = 3
    
tile_symbols = {
    TileType.path: '.',
    TileType.wall: '#',
    TileType.player: '@'
}

is_solid = {
    TileType.path: False,
    TileType.wall: True
}
    
class Tile:
    def __init__(self, object):
        self.solid = is_solid[object]
        self.symbol = tile_symbols[object]