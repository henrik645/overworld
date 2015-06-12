"""
This file includes several helpers used in main.py that handles commands,
checks directions, and more.
"""

import curses
import sys

import screen

directions = {
    curses.KEY_UP,
    curses.KEY_DOWN,
    curses.KEY_LEFT,
    curses.KEY_RIGHT
}

def exit_game(stdscr, status_screen):
    screen.end(stdscr)
    screen.end(status_screen)
    sys.exit(0)

def get_direction(stdscr, status_screen):
    directions = [
        curses.KEY_UP,
        curses.KEY_DOWN,
        curses.KEY_LEFT,
        curses.KEY_RIGHT
    ]
    while True:
        status.status(status_screen, "Which direction? ")
        key = stdscr.getch()
        if key in directions:
            return key
            
def check_direction(direction, character, width, height):
    if direction == curses.KEY_UP:
        return character.y_pos > 0
    elif direction == curses.KEY_DOWN:
        return character.y_pos < height - 1
    elif direction == curses.KEY_LEFT:
        return character.x_pos > 0
    elif direction == curses.KEY_RIGHT:
        return character.x_pos < width - 1
    else:
        raise NotImplementedError('Not a valid direction')
        
def get_square_next_to(character, direction, level):
    if direction == curses.KEY_UP:
        return level.map[character.y_pos - 1][character.x_pos]
    elif direction == curses.KEY_DOWN:
        return level.map[character.y_pos + 1][character.x_pos]
    elif direction == curses.KEY_LEFT:
        return level.map[character.y_pos][character.x_pos - 1]
    elif direction == curses.KEY_RIGHT:
        return level.map[character.y_pos][character.x_pos + 1]
    else:
        raise NotImplementedError('Not a valid direction')
        
def move_character(character, direction, step=1):
    if direction == curses.KEY_UP:
        character.y_pos -= step
    elif direction == curses.KEY_DOWN:
        character.y_pos += step
    elif direction == curses.KEY_LEFT:
        character.x_pos -= step
    elif direction == curses.KEY_RIGHT:
        character.x_pos += step
    else:
        raise NotImplementedError('Not a valid direction')

def handle_input(key, character, level, level_width, level_height, stdscr, status_screen):
    if key in directions:
        if check_direction(key, character, level_width, level_height):
            if get_square_next_to(character, key, level).solid == False:
                move_character(character, key)
                
    elif key == ord('q'):
        exit_game(stdscr, status_screen)
        
    elif key == ord('s'):
        save_game = save.Save(character, level)
        save_game.save_game(config['save_file'])
        exit_game(stdscr, status_screen)
        
    elif key == ord('o'):
        direction = get_direction(stdscr, status_screen)
        if direction == curses.KEY_UP:
            if character.y_pos > 0:
                if level.map[character.y_pos - 1][character.x_pos].object == tile.TileType.door:
                    level.map[character.y_pos - 1][character.x_pos] = tile.Tile(tile.TileType.door_open)
                else:
                    status.status(status_screen, "There is not a door there.")
        elif direction == curses.KEY_DOWN:
            if character.y_pos < level_height - 1:
                if level.map[character.y_pos + 1][character.x_pos].object == tile.TileType.door:
                    level.map[character.y_pos + 1][character.x_pos].symbol = tile.TileType.door_open
                else:
                    status.status(status_screen, "There is not a door there.")
        elif direction == curses.KEY_LEFT:
            if character.x_pos > 0:
                if level.map[character.y_pos][character.x_pos - 1].object == tile.TileType.door:
                    level.map[character.y_pos][character.x_pos - 1] = tile.Tile(tile.TileType.door_open)
                else:
                    status.status(status_screen, "There is not a door there.")
        elif direction == curses.KEY_RIGHT:
            if character.x_pos < level_width - 1:
                if level.map[character.y_pos][character.x_pos + 1].object == tile.TileType.door:
                    level.map[character.y_pos][character.x_pos + 1] = tile.Tile(tile.TileType.door_open)
                else:
                    status.status(status_screen, "There is not a door there.")