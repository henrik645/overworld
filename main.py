"""
This file contains the main loop of the program
"""

import curses
import json
import os

import screen
import world
import player
import status
import save
import tile
import helpers

level_width = 80
level_height = 20

with open('config.json', 'r') as file:
    config = json.loads(file.read())

stdscr = screen.init_screen()
status_screen = status.init_screen(level_width, level_height)

if os.path.isfile(config['save_file']):
    save_game = save.load_game(config['save_file'])
    level = save_game.world_save
    character = save_game.player_save
    save_exists = True
else:
    level = world.Level(level_width, level_height)
    character = player.Player(10, 10, 5, 5)
    save_exists = False

while True: #Main loop
    screen.update_screen(stdscr, level, character)
    screen.update_player_status(status_screen, character)
    character.check()
    if not character.alive:
        status.status(status_screen, "You die...")
        if save_exists:
            os.remove(config['save_file'])
        break
        
    key = stdscr.getch()
    helpers.handle_input(key, character, level, level_width, level_height, stdscr, status_screen)