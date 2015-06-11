"""
This file defines all functions which updates the status line
"""

import curses

import screen

log = []

def init_screen(width, height):
    return curses.newwin(2, width, height, 0)

def status(status_screen, message):
    screen.update_status_line(status_screen, message)
    log.append(message)