#------------------------------------------------------------------------------
#CURRENT STATE
#------------------------------------------------------------------------------

# This folder contains the class for the c_state class which will help manage and return all of the current settings
#between different program windows.

#------------------------------------------------------------------------------
#libaries
#------------------------------------------------------------------------------
import pygame #GUI

#------------------------------------------------------------------------------
#initialisation
#------------------------------------------------------------------------------
pygame.init()

#------------------------------------------------------------------------------
#current state (c_state) class
#------------------------------------------------------------------------------

class c_state:
    def __init__(self, window_width, window_height):

        #attributes
        self.window_width = window_width
        self.window_height = window_height
        self.audio_level = 50
        self.feedback_on = True            #default values
        self.time_amount = 10