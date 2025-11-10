#------------------------------------------------------------------------------
#WIN STATISTICS WINDOW
#------------------------------------------------------------------------------

#This window contains the win statistics for the user. It will display the user's
#wins, draws (stalemates), and losses.

#------------------------------------------------------------------------------
#libaries
#------------------------------------------------------------------------------
import pygame #GUI
import sys    #Clean shutdown.

#------------------------------------------------------------------------------
#File imports
#------------------------------------------------------------------------------
from utils.scalable_font import scaled_font #Font is proportional to window size.
from utils.UI.display_box import Display_box
from utils.UI.button import Button 
from resources.colours import *

#------------------------------------------------------------------------------
#Initialisation
#------------------------------------------------------------------------------
pygame.init() #Pygame requires

#------------------------------------------------------------------------------
#Win statistics window function
#------------------------------------------------------------------------------
def win_stats(current_settings): #The parameters: cw = Current width, ch = Current height (Referring to the size of the display).

    #important locals
    placeholder_number = 0

    #Display configs
    window = pygame.display.set_mode((current_settings.window_width, current_settings.window_height)) #Sets the size of the window to be the current width and height.
    pygame.display.set_caption("BLOCKADE (win statistics)") #Allows user to see game name to be clear what window they are in.
    
    #creating display boxes
    win_stats_title_db = Display_box("WIN STATISTICS",current_settings.window_width, current_settings.window_height,0.25,0.1,0.5,0.1,scaled_font(current_settings.window_height),DARKBLUE,WHITE) #Title at the top of the screen

    wins_db = Display_box(f"WINS:{placeholder_number}",current_settings.window_width, current_settings.window_height,0.05,0.225,0.3,0.6,scaled_font(current_settings.window_height),DARKBLUE,WHITE)

    draws_db = Display_box(f"DRAWS:{placeholder_number}",current_settings.window_width, current_settings.window_height,0.35,0.225,0.3,0.6,scaled_font(current_settings.window_height),DARKBLUE,WHITE)    #Big boxes showing win amount, draw amount and loss amount.

    losses_db = Display_box(f"LOSSES:{placeholder_number}",current_settings.window_width, current_settings.window_height,0.64,0.225,0.3,0.6,scaled_font(current_settings.window_height),DARKBLUE,WHITE)

    #creating buttons
    return_button = Button("return to main menu",current_settings.window_width, current_settings.window_height, 0.25, 0.85, 0.5, 0.1,scaled_font(current_settings.window_height),DARKBLUE,LIGHTBLUE,WHITE) #Button that lets the user return to the main menu.
   
    #lists for easy management and drawing
    display_box_list = [win_stats_title_db, wins_db, draws_db, losses_db] #Display box list lets the program loop through display boxes to iteratively draw them.

    button_list = [return_button] #Button list lets the program loop through buttons to iteratively draw and interact with them.

    #window loop #While the variable "active" is true the win statistics function won't end unless forcefully exited.
    active = True
    while active:
        event_handler = pygame.event.get() #The event handler checks through every single possible pygame event.
        mouse_position = pygame.mouse.get_pos() #Allows the tracking of the mouse position.
        for event in event_handler:
            if event.type == pygame.QUIT:    #If you click on the X in the top right it will exit the software.
                sys.exit()
        
        for b in button_list:  #Loop through every button to give each one a unique function.
            b.detect_mouse(mouse_position)
            b.check_for_click(event_handler) #Check for where the mouse is and if it has clicked the button.
            if b.clicked == True:
                if b == return_button:
                    return (current_settings)  #Updates the resolution in main menu so the windows are the same size.
            
        #drawing
        window.fill((0,0,0))  #fill in the background
        for b in button_list:
            b.b_draw(window) #loop through all of the buttons and draw them onto the window

        for b in display_box_list: #loop through all of the display boxes and draw them onto the window.
            b.b_draw(window)

        pygame.display.update() #Updates the frames in the window.