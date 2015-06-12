"""
This file defines a class named Tile and functions associated with it.
The Tile class is used for representing tiles in the game world.
"""

class TileType:
    path = 1
    wall = 2
    player = 3
    door = 4
    door_open = 5
    
tile_symbols = {
    TileType.path: '.',
    TileType.wall: '#',
    TileType.player: '@',
    TileType.door: '+',
    TileType.door_open: '-'
}

is_solid = {
    TileType.path: False,
    TileType.wall: True,
    TileType.door: True,
    TileType.door_open: False
}
    
class Tile:
    def __init__(self, object):
        self.solid = is_solid[object]
        self.symbol = tile_symbols[object]
        self.object = object