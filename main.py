"""
This file contains the main loop of the program
"""

import curses

import screen
import world
import player
import status

level_width = 80
level_height = 20

stdscr = screen.init_screen()
status_screen = status.init_screen(level_width, level_height)

level = world.Level(level_width, level_height)
character = player.Player(10, 10, 5, 5)

while True: #Main loop
    screen.update_screen(stdscr, level, character)
    screen.update_player_status(status_screen, character)
    character.check()
    if not character.alive:
        status.status(status_screen, "You die...")
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

screen.end(stdscr)
screen.end(status_screen)