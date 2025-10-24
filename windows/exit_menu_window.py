#------------------------------------------------------------------------------
#EXIT MENU
#------------------------------------------------------------------------------

#This menu is literally just a confirmation that you understand the consiquences of leaving an active game
#without finishing it

#------------------------------------------------------------------------------
#libaries
#------------------------------------------------------------------------------
import pygame #GUI
import sys #Clean Shutdown

#------------------------------------------------------------------------------
#File imports
#------------------------------------------------------------------------------
from utils.scalable_font import scaled_font #Font is proportional to window size.
from utils.UI.button import Button
from resources.colours import *

#------------------------------------------------------------------------------
#initialisation
#------------------------------------------------------------------------------
pygame.init()

#------------------------------------------------------------------------------
#exit menu window function
#------------------------------------------------------------------------------
def exit_menu():
    #display configs
    pygame.display.set_mode((500,500)) #PLACEHOLDER VALUES this will 100% change bc of settings and resizing
    pygame.display.set_caption("BLOCKADE (exit menu)") #Allows user to see game name and be clear what window they are in.
    
    #window loop
    active = True
    while active:
        event_handler = pygame.event.get() #The event handler checks through every single possible pygame event.
        mouse_position = pygame.mouse.get_pos() #Allows the tracking of the mouse position.
        for event in event_handler:
            if event.type == pygame.QUIT:    #If you click on the X in the top right it will exit the software.
                sys.exit()