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
from windows.main_menu_window import main_menu

#------------------------------------------------------------------------------
#Initialisation
#------------------------------------------------------------------------------
pygame.init() #Required for pygame to work in the file.
resolution = pygame.display.Info() #This gets the current width and height of the users monitor / screen.

#------------------------------------------------------------------------------
#Globals
#------------------------------------------------------------------------------
current_w, current_h = resolution.current_w, resolution.current_h #Storing the width and height in the currentw/h variables.

#current_w, current_h = 1280,800 #will delete at some point is just for debugging

#------------------------------------------------------------------------------
#Main code
#------------------------------------------------------------------------------
main_menu(current_w,current_h) #Always opens to main menu first. 

sys.exit() #This is just so that there is always a clean exit where everything gets shut down.