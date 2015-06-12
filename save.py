"""
This file defines functions used for saving and loading the game
"""

import pickle

import player
import world

class Save: #Class used by Pickle to save the entire game as a single object
    def __init__(self, player_save, world_save):
        self.player_save = player_save
        self.world_save = world_save
        
    def save_game(self, file):
        with open(file, 'wb') as file:
            pickle.dump(self, file)
            
def load_game(file):
    with open(file, 'rb') as file:
        return pickle.load(file)