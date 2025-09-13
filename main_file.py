#main game file where the program will start from and where the main game will be played from.

#libraries
import pygame
import sys

#file imports
from windows.main_menu_window import main_menu

#initialisation
pygame.init()

#globals
resolution = pygame.display.Info()
current_w, current_h = resolution.current_w, resolution.current_h

#main code
main_menu() #always open to main menu first

pygame.quit()
sys.exit()