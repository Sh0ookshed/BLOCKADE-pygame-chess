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
from resources.colours import *

from utils.configs.scalable_font import scaled_font #Font is proportional to window size.

from utils.UI.display_box import Display_box
from utils.UI.button import Button


#------------------------------------------------------------------------------
#initialisation
#------------------------------------------------------------------------------
pygame.init()

#------------------------------------------------------------------------------
#exit menu window function
#------------------------------------------------------------------------------
def exit_menu(cw,ch): #The parameters: cw = Current width, ch = Current height (Referring to the size of the display).
   
    #important locals
    choice = False #choice returns at the end of the function
    
    #display configs
    window = pygame.display.set_mode((cw,ch)) 
    pygame.display.set_caption("BLOCKADE (exit menu)") #Allows user to see game name and be clear what window they are in.
    
    #creating display boxes
    exit_q_db = Display_box("Are you sure you want to exit? If you exit you automatically resign the game, and it will be recorded as a loss!",cw,ch,0.2,0.2,0.6,0.6,scaled_font(ch),DARKBLUE,WHITE)

    #creating buttons
    yes_button = Button("Yes",cw,ch,0.2,0.8,0.3,0.1,scaled_font(ch),DARKBLUE,LIGHTBLUE,WHITE) #Yes button user has the option to click, if clicked exit_menu will return True
    no_button = Button("No",cw,ch,0.5,0.8,0.3,0.1,scaled_font(ch),DARKBLUE,LIGHTBLUE,WHITE) #No button user has the option to click, if clicked exit_menu will return False

    #Lists for easy management and drawing
    button_list = [yes_button,no_button]

    display_box_list = [exit_q_db]

    #window loop
    active = True

    while active:
        event_handler = pygame.event.get() #The event handler checks through every single possible pygame event.
        mouse_position = pygame.mouse.get_pos() #Allows the tracking of the mouse position.

        for event in event_handler:

            if event.type == pygame.QUIT:    #If you click on the X in the top right it will exit the software.
                sys.exit()

        for b in button_list: #Loop through every button to give each one a unique function
                b.detect_mouse(mouse_position)

                b.check_for_click(event_handler)  #Check for where the mouse is and if it has clicked the button.
                if b.clicked == True:
                    
                    if b == yes_button:
                        choice = True
                    return choice
        #drawing
        window.fill((0,0,0)) #fill in the background

        for b in button_list: #loop through all of the buttons and draw them onto the window.
            b.b_draw(window)

        for b in display_box_list: #loop through all of the display boxes and draw them onto the window.
            b.b_draw(window)

        pygame.display.update() #Updates the frames in the window.