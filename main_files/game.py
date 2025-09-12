#main game file containing the GUI and where the main game will be played from.

#libraries
import pygame
import os

#file imports
from windows.end_of_game_windows import you_win,you_draw,you_lose
from windows.exit_menu_window import exit_menu
from windows.feedback_window import feedback
from windows.gameplay_window import gameplay
from windows.main_menu_window import main_menu
from windows.settings_window import settings
from windows.win_statistics_window import win_stats

#initialisation
pygame.init()

#globals
resolution = pygame.display.Info()
screen_w, screen_h = resolution.current_w, resolution.current_h

#main code
main_menu()