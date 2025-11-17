#------------------------------------------------------------------------------
#MAIN FILE
#------------------------------------------------------------------------------

#This is where the program will start from, it immediately loads the user into the main menu function 
#allowing the user to go to any part of the program.

#------------------------------------------------------------------------------
#Libraries
#------------------------------------------------------------------------------
import pygame #GUI
import sys    #For shutting down the program.

#------------------------------------------------------------------------------
#File imports
#------------------------------------------------------------------------------
from utils.configs.current_state import c_state

from windows.main_menu_window import main_menu

#------------------------------------------------------------------------------
#Initialisation
#------------------------------------------------------------------------------
pygame.init() #Required for pygame to work in the file.
resolution = pygame.display.Info() #This gets the current width and height of the users monitor / screen.

#------------------------------------------------------------------------------
#Globals
#------------------------------------------------------------------------------
settings_configs = c_state(resolution.current_w, resolution.current_h)

#------------------------------------------------------------------------------
#Main code
#------------------------------------------------------------------------------
main_menu(settings_configs) #Always opens to main menu first. 

sys.exit() #This is just so that there is always a clean exit where everything gets shut down.