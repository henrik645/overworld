"""
This file defines the main player class and associated functions
"""

class Player:
    def __init__(self, hp, defense, x_pos, y_pos):
        self.hp = hp
        self.defense = defense
        self.x_pos = x_pos
        self.y_pos = y_pos
        self.alive = True
        
    def check(self): #Checks HP for negative values
        if self.hp <= 0:
            self.alive = False