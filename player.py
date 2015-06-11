"""
This file defines the main player class and associated functions
"""

import status

def get_xp_required(level): #Returns the amount of XP required for a certain level
    if level <= 10:
        return level * 50
    else:
        return level * 100

class Player:
    def __init__(self, hp, defense, x_pos, y_pos):
        self.hp = hp
        self.defense = defense
        self.x_pos = x_pos
        self.y_pos = y_pos
        self.alive = True
        self.dungeon_level = 0
        self.level = 1
        self.xp = 0
        
    def check(self, status_screen): #Checks HP for negative values
        if self.hp <= 0:
            self.alive = False
            
        if self.xp > get_xp_required(self.level + 1):
            while self.xp > get_xp_required(self.level + 1):
                self.level += 1
                self.xp -= get_xp_required(self.level)
            status.status(status_screen, "Welcome to experience level " + str(self.level) + ".")