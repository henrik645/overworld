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

def get_direction(stdscr, status_screen):
    directions = {
        curses.KEY_UP: "up",
        curses.KEY_DOWN: "down",
        curses.KEY_LEFT: "left",
        curses.KEY_RIGHT: "right"
    }
    while True:
        status.status(status_screen, "Which direction? ")
        key = stdscr.getch()
        if key in directions:
            return directions[key]

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
    level.map[5][10] = tile.Tile(tile.TileType.door)
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
    if key == curses.KEY_UP:
        if character.y_pos > 0:
            if level.map[character.y_pos - 1][character.x_pos].solid == False:
                character.y_pos -= 1
    elif key == curses.KEY_DOWN:
        if character.y_pos < level_height - 1: #Minus once since coordinates start at 0 instead of 1
            if level.map[character.y_pos + 1][character.x_pos].solid == False:
                character.y_pos += 1
    elif key == curses.KEY_LEFT:
        if character.x_pos > 0:
            if level.map[character.y_pos][character.x_pos - 1].solid == False:
                character.x_pos -= 1
    elif key == curses.KEY_RIGHT:
        if character.x_pos < level_width - 1: #Minus once since coordinates start at 0 instead of 1
            if level.map[character.y_pos][character.x_pos + 1].solid == False:
                character.x_pos += 1
    elif key == ord('q'):
        break
    elif key == ord('s'):
        save_game = save.Save(character, level)
        save_game.save_game(config['save_file'])
        break
    elif key == ord('o'):
        direction = get_direction(stdscr, status_screen)
        if direction == "up":
            if character.y_pos > 0:
                if level.map[character.y_pos - 1][character.x_pos].object == tile.TileType.door:
                    level.map[character.y_pos - 1][character.x_pos] = tile.Tile(tile.TileType.door_open)
                else:
                    status.status(status_screen, "There is not a door there.")
        elif direction == "down":
            if character.y_pos < level_height - 1:
                if level.map[character.y_pos + 1][character.x_pos].object == tile.TileType.door:
                    level.map[character.y_pos + 1][character.x_pos].symbol = tile.TileType.door_open
                else:
                    status.status(status_screen, "There is not a door there.")
        elif direction == "left":
            if character.x_pos > 0:
                if level.map[character.y_pos][character.x_pos - 1].object == tile.TileType.door:
                    level.map[character.y_pos][character.x_pos - 1] = tile.Tile(tile.TileType.door_open)
                else:
                    status.status(status_screen, "There is not a door there.")
        elif direction == "right":
            if character.x_pos < level_width - 1:
                if level.map[character.y_pos][character.x_pos + 1].object == tile.TileType.door:
                    level.map[character.y_pos][character.x_pos + 1] = tile.Tile(tile.TileType.door_open)
                else:
                    status.status(status_screen, "There is not a door there.")

screen.end(stdscr)
screen.end(status_screen)