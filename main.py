"""
This file contains the main loop of the program
"""

import time
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
player = player.Player(10, 10, 5, 5)

while True: #Main loop
    screen.update_screen(stdscr, level, player)
    screen.update_player_status(status_screen, player)
    key = stdscr.getch()
    if key == curses.KEY_UP:
        if player.y_pos > 0:
            player.y_pos -= 1
    elif key == curses.KEY_DOWN:
        if player.y_pos < level_height - 1: #Minus once since coordinates start at 0 instead of 1
            player.y_pos += 1
    elif key == curses.KEY_LEFT:
        if player.x_pos > 0:
            player.x_pos -= 1
    elif key == curses.KEY_RIGHT:
        if player.x_pos < level_width - 1: #Minus once since coordinates start at 0 instead of 1
            player.x_pos += 1
    elif key == ord('q'):
        break

screen.end(stdscr)
screen.end(status_screen)