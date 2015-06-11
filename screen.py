"""
This file defines all functions associated with screen handling
"""

import curses
import tile

def init_screen():
    screen = curses.initscr()
    screen.keypad(True)
    curses.cbreak()
    curses.noecho()
    curses.curs_set(False)
    
    return screen
    
def end(screen):
    screen.keypad(False)
    curses.nocbreak()
    curses.echo()
    curses.endwin()
    curses.curs_set(True)

def update_screen(screen, level, player=None):
    for y in range(level.height):
        for x in range(level.width):
            screen.addstr(y, x, level.map[y][x].symbol)
    
    if player is not None: #A player needs to be plotted
        screen.addstr(player.y_pos, player.x_pos, tile.tile_symbols[tile.TileType.player])
    screen.refresh()