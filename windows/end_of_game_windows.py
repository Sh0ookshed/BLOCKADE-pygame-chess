#------------------------------------------------------------------------------
#END OF GAME WINDOWS
#------------------------------------------------------------------------------

#Contains the multiple functions for the end of game windows. These windows show the user whether you have won,
#drawn (stalemate), or lost the game of chess just played.

#------------------------------------------------------------------------------
#libaries
#------------------------------------------------------------------------------
import pygame #GUI
import sys #Clean shutdown

#------------------------------------------------------------------------------
#File imports
#------------------------------------------------------------------------------
from resources.colours import *

from utils.configs.scalable_font import scaled_font #Font is proportional to window size.

from utils.UI.button import Button

#------------------------------------------------------------------------------
#initialisation
#------------------------------------------------------------------------------
pygame.init()

#------------------------------------------------------------------------------
#win scenario function
#------------------------------------------------------------------------------
def you_win():
    #display configs
    pygame.display.set_mode((500,500)) #PLACEHOLDER VALUES this will 100% change bc of settings and resizing
    pygame.display.set_caption("BLOCKADE (you win!)") #allows user to see game name and be clear what window they are in
    
    #window loop
    active = True
    while active:
        event_handler = pygame.event.get() #The event handler checks through every single possible pygame event.
        mouse_position = pygame.mouse.get_pos() #Allows the tracking of the mouse position.
        for event in event_handler:
            if event.type == pygame.QUIT:    #If you click on the X in the top right it will exit the software.
                sys.exit()

#------------------------------------------------------------------------------
#draw scenario function
#------------------------------------------------------------------------------
def you_draw():
    #display configs
    pygame.display.set_mode((500,500)) #PLACEHOLDER VALUES this will 100% change bc of settings and resizing
    pygame.display.set_caption("BLOCKADE (you draw!)") #allows user to see game name and be clear what window they are in
    
    #window loop
    active = True

    while active:
        event_handler = pygame.event.get() #The event handler checks through every single possible pygame event.
        mouse_position = pygame.mouse.get_pos() #Allows the tracking of the mouse position.

        for event in event_handler:

            if event.type == pygame.QUIT:    #If you click on the X in the top right it will exit the software.
                sys.exit()

#------------------------------------------------------------------------------
#lose scenario function
#------------------------------------------------------------------------------
def you_lose():
    #display configs
    pygame.display.set_mode((500,500)) #PLACEHOLDER VALUES this will 100% change bc of settings and resizing
    pygame.display.set_caption("BLOCKADE (you lost!)") #allows user to see game name and be clear what window they are in
    
    #window loop
    active = True

    while active:
        event_handler = pygame.event.get() #The event handler checks through every single possible pygame event.
        mouse_position = pygame.mouse.get_pos() #Allows the tracking of the mouse position.

        for event in event_handler:
            
            if event.type == pygame.QUIT:    #If you click on the X in the top right it will exit the software.
                sys.exit()