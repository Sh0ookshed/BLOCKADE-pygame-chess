#------------------------------------------------------------------------------
#FEEDBACK WINDOW
#------------------------------------------------------------------------------

#This is where the user will recieve post game feedback after the chess game they are playing has been resolved

#------------------------------------------------------------------------------
#libaries
#------------------------------------------------------------------------------
import pygame #GUI
import sys    #Clean shutdown

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
#feedback window function
#------------------------------------------------------------------------------
def feedback():
    #display configs
    pygame.display.set_mode((500,500)) #PLACEHOLDER VALUES this will 100% change bc of settings and resizing
    pygame.display.set_caption("BLOCKADE (feedback)") #Allows user to see game name and be clear what window they are in.
    
    #window loop
    active = True

    while active:
        event_handler = pygame.event.get() #The event handler checks through every single possible pygame event.
        mouse_position = pygame.mouse.get_pos() #Allows the tracking of the mouse position.

        for event in event_handler:
            
            if event.type == pygame.QUIT:    #also need to work out how to down the whole program from exit
                sys.exit()