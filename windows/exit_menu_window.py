#contains the function for the exit menu window

#libaries
import pygame
import sys

#other file imports
from utils.scalable_font import scaled_font
from utils.button import Button
from resources.colours import *

#initialisation
pygame.init()

#exit menu window function
def exit_menu():
    #display configs
    pygame.display.set_mode((500,500)) #PLACEHOLDER VALUES this will 100% change bc of settings and resizing
    pygame.display.set_caption("BLOCKADE (exit menu)") #allows user to see game name and be clear what window they are in
    
    #window loop
    active = True
    while active:
        event_handler = pygame.event.get()
        for event in event_handler:
            if event.type == pygame.QUIT:    #also need to work out how to down the whole program from exit
                sys.exit()