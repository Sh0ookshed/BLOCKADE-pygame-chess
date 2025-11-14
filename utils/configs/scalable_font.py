#------------------------------------------------------------------------------
#SCALABLE FONT
#------------------------------------------------------------------------------

#Contains the function for the scalable font that changes size depending on window size.

#------------------------------------------------------------------------------
#libraries
#------------------------------------------------------------------------------
import pygame #GUI

#initialisation
pygame.init() 

#------------------------------------------------------------------------------
#Scalable font function
#------------------------------------------------------------------------------
def scaled_font(height):
    font = pygame.font.Font(None,int(height*0.08))  #font size is 8% of the height of the window.
    return font