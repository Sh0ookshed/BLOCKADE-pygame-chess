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

from utils.UI.display_box import Display_box
from utils.UI.button import Button

from utils.UI.chess_UI.chess_board import create_chess_board

from resources.colours import *

#------------------------------------------------------------------------------
#initialisation
#------------------------------------------------------------------------------
pygame.init()

#------------------------------------------------------------------------------
#gameplay window function
#------------------------------------------------------------------------------
def gameplay(current_settings):  #The parameters: cw = Current width, ch = Current height (Referring to the size of the display).

    #important locals
    chess_board_surface = pygame.Surface((current_settings.window_width*0.665,current_settings.window_height*0.675))
    chess_board = create_chess_board(chess_board_surface.get_width(),chess_board_surface.get_height(),WHITE,GREY)

    #display configs
    window = pygame.display.set_mode((current_settings.window_width, current_settings.window_height)) ##Sets the size of the window to be the current width and height.
    pygame.display.set_caption("BLOCKADE (gameplay)") #Allows user to see game name and be clear what window they are in.
    
    #creating display boxes
    feedback_display_placeholder = Display_box("feedback placeholder",current_settings.window_width, current_settings.window_height, 0.675, 0.3, 0.3, 0.475,scaled_font(current_settings.window_height),DARKBLUE,WHITE)

    time_display = Display_box(f"time: {current_settings.time_amount}",current_settings.window_width, current_settings.window_height, 0.675, 0.05, 0.3, 0.25,scaled_font(current_settings.window_height),DARKBLUE,WHITE)
    
    vs_placeholder = Display_box("BOT VS USER (PLACEHOLDER)",current_settings.window_width, current_settings.window_height, 0, 0.05, 0.675, 0.24,scaled_font(current_settings.window_height),DARKBLUE,WHITE)

    #creating buttons
    return_button = Button("return to main menu",current_settings.window_width, current_settings.window_height, 0.675, 0.775, 0.14, 0.2,scaled_font(current_settings.window_height),DARKBLUE,LIGHTBLUE,WHITE) #Button that lets the user return to the main menu.

    offer_draw_button = Button("offer draw",current_settings.window_width, current_settings.window_height, 0.825, 0.775, 0.15, 0.2,scaled_font(current_settings.window_height),DARKBLUE,LIGHTBLUE,WHITE) #Button that lets the user return to the main menu.


    #lists for easy management and drawing
    button_list = [return_button,offer_draw_button] #Button list lets the program loop through buttons to iteratively draw and interact with them.

    display_box_list = [feedback_display_placeholder,time_display,vs_placeholder] #Display box list lets the program loop through display boxes to iteratively draw them.
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
                    return (current_settings)
            
        #drawing
        window.fill((0,0,0)) #fill in the background
        chess_board_surface.fill((125,100,0))

        for b in button_list: #loop through all of the buttons and draw them onto the window.
            b.b_draw(window)

        for b in display_box_list: #loop through all of the display boxes and draw them onto the window.
            b.b_draw(window)

        for row in chess_board:
            for square in row:
                square.draw_box(chess_board_surface)

        window.blit(chess_board_surface,(0.005*current_settings.window_width,0.3*current_settings.window_height))

        pygame.display.flip() #Updates the frames in the window.