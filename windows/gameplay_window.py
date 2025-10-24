#------------------------------------------------------------------------------
#GAMEPLAY WINDOW
#------------------------------------------------------------------------------

#contains the function for the gameplay window. This is where the user will actually play chess against an algorithm
#on a virtual chess board. This file will link to rust backend as well as providing the same pygame GUI.

#------------------------------------------------------------------------------
#libaries
#------------------------------------------------------------------------------
import pygame #GUI
import sys    #Clean shutdown

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
#gameplay window function
#------------------------------------------------------------------------------
def gameplay(cw,ch):  #The parameters: cw = Current width, ch = Current height (Referring to the size of the display).
    #display configs
    window = pygame.display.set_mode((cw,ch)) ##Sets the size of the window to be the current width and height.
    pygame.display.set_caption("BLOCKADE (gameplay)") #Allows user to see game name and be clear what window they are in.
    
    #creating buttons
    return_button = Button("return to main menu",cw,ch, 0.4, 0.4, 0.2, 0.2,scaled_font(ch),DARKBLUE,LIGHTBLUE,WHITE) #Button that lets the user return to the main menu.

    button_list = [return_button] #Button list lets the program loop through buttons to iteratively draw and interact with them.

    #window loop
    active = True
    while active:
        event_handler = pygame.event.get() #The event handler checks through every single possible pygame event.
        mouse_position = pygame.mouse.get_pos() #Allows the tracking of the mouse position.
        for event in event_handler:
            if event.type == pygame.QUIT:    #If you click on the X in the top right it will exit the software.
                sys.exit()
        
        for b in button_list:     #Loop through every button to give each one a unique function.
            b.detect_mouse(mouse_position)
            b.check_for_click(event_handler)  #Check for where the mouse is and if it has clicked the button.
            if b.clicked == True:
                if b == return_button:
                    return (cw,ch)
            
        #drawing
        window.fill((0,0,0)) #fill in the background

        for b in button_list: #loop through all of the buttons and draw them onto the window.
            b.b_draw(window)

        pygame.display.update() #Updates the frames in the window.