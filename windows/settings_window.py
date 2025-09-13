#contains the function for the settings window

#libaries
import pygame
import sys

#initialisation
pygame.init()

#settings menu window function
def settings():
    #display configs
    pygame.display.set_mode((500,500)) #PLACEHOLDER VALUES this will 100% change bc of settings and resizing
    pygame.display.set_caption("chess game (settings)") #"chess game" is also placeholder until better name
    
    #window loop
    active = True
    while active:
        for event in pygame.event.get():
            if event.type == pygame.QUIT():    #also need to work out how to down the whole program from exit
                active = False