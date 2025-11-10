#------------------------------------------------------------------------------
#MAIN MENU WINDOW
#------------------------------------------------------------------------------

#contains the function for the main menu window. This is where the user interacts with at the start of
#the software loading and furthermore is mainly used as a hub to get between different parts of the software.

#libaries
import pygame #GUI
import sys    #Clean shutdown

#------------------------------------------------------------------------------
#File imports
#------------------------------------------------------------------------------
from windows.gameplay_window import gameplay #Importing the windows.
from windows.settings_window import settings
from windows.win_statistics_window import win_stats

from utils.scalable_font import scaled_font #Font is proportional to window size.
from utils.random_pick import rand_item

from utils.UI.display_box import Display_box
from utils.UI.button import Button                

from resources.colours import *
from resources.chess_tips import advice_list #This list just contains loads of tips/hints for the random generator.

#------------------------------------------------------------------------------
#initialisation
#------------------------------------------------------------------------------
pygame.init()

#------------------------------------------------------------------------------
#main menu window function
#------------------------------------------------------------------------------
def main_menu(current_settings): #The parameters: cw = Current width, ch = Current height (Referring to the size of the display).
    
    #display configs
    window = pygame.display.set_mode((current_settings.window_width, current_settings.window_height)) #Sets the size of the window to be the current width and height.
    pygame.display.set_caption("BLOCKADE (main menu)") #Allows user to see game name and be clear what window they are in.
    
    #loading assets
    background = pygame.image.load("assets/BLOCKADE BACKGROUND.png").convert()
    background = pygame.transform.scale(background, (current_settings.window_width, current_settings.window_height))
    
    logo = pygame.image.load("assets/BLOCKADE LOGO.png").convert()
    logo = pygame.transform.scale(logo, (current_settings.window_width*0.5, current_settings.window_height*0.433))
    
    #creating display boxes
    advice_db = Display_box("Useful hints and tricks:", current_settings.window_width, current_settings.window_height, 0.45, 0.499 ,0.5, 0.1,scaled_font(current_settings.window_height),DARKBLUE,WHITE)

    #creating buttons
    play_button = Button("play",current_settings.window_width, current_settings.window_height, 0.025, 0.033, 0.4, 0.2,scaled_font(current_settings.window_height),DARKBLUE,LIGHTBLUE,WHITE) #Takes the user to the gameplay window.

    win_stats_button = Button("view win statistics",current_settings.window_width, current_settings.window_height, 0.025, 0.266, 0.4, 0.2,scaled_font(current_settings.window_height),DARKBLUE,LIGHTBLUE,WHITE) #Takes the user to the win statistics window.

    settings_menu_button = Button("settings",current_settings.window_width, current_settings.window_height, 0.025, 0.499, 0.4, 0.2,scaled_font(current_settings.window_height),DARKBLUE,LIGHTBLUE,WHITE) #Takes the user to the settings window.

    exit_button = Button("exit",current_settings.window_width, current_settings.window_height, 0.025, 0.732, 0.4, 0.2,scaled_font(current_settings.window_height),DARKBLUE,LIGHTBLUE,WHITE) #Shuts down the program 

    advice_button = Button(rand_item(advice_list),current_settings.window_width, current_settings.window_height, 0.45, 0.599 ,0.5, 0.333,scaled_font(current_settings.window_height),DARKBLUE,LIGHTBLUE,WHITE) #Shows random chess tips and facts to the user. (Can be clicked to update)

    #lists for easy management and drawing
    display_box_list = [advice_db]
    
    button_list = [play_button,win_stats_button,settings_menu_button,exit_button,advice_button] #Button list lets the program loop through buttons to iteratively draw and interact with them.

    #window loop #While the variable "active" is true the win statistics function won't end unless forcefully exited.
    active = True
    while active:
        event_handler = pygame.event.get() #The event handler checks through every single possible pygame event.
        mouse_position = pygame.mouse.get_pos() #Allows the tracking of the mouse position.

        for event in event_handler:
            if event.type == pygame.QUIT:    #If you click on the X in the top right it will exit the software.
                sys.exit()
        
        for b in button_list:   #Loop through every button to give each one a unique function.
            b.detect_mouse(mouse_position)
            b.check_for_click(event_handler) #Check for where the mouse is and if it has clicked the button.
            if b.clicked == True:

                if b == play_button:
                    current_settings = gameplay(current_settings)
                    window = pygame.display.set_mode((current_settings.window_width, current_settings.window_height)) #Updates the resolution in main menu after returning from the relevant window so the windows are the same size.
                    cw = pygame.display.get_surface().get_width() #Updates the current width variable to be the same as the actual width
                    ch = pygame.display.get_surface().get_height() #Updates the current height variable to be the same as the actual height
                    for r in button_list:
                        r.resize(current_settings.window_width, current_settings.window_height,scaled_font(current_settings.window_height)) #Update all buttons to be proportional to the new resolution.
                    
                    for r in display_box_list:
                        r.resize(current_settings.window_width, current_settings.window_height,scaled_font(current_settings.window_height)) #Update all display boxes to be proportional to the new resolution.
                        
                    logo = pygame.transform.scale(logo, (current_settings.window_width*0.5, current_settings.window_height*0.433))
                    pygame.display.set_caption("BLOCKADE (main menu)") #Makes sure the caption returns to Blockade (main menu)

                elif b == win_stats_button:
                    current_settings = win_stats(current_settings)
                    window = pygame.display.set_mode((current_settings.window_width, current_settings.window_height)) 
                    for r in button_list:
                        r.resize(current_settings.window_width, current_settings.window_height,scaled_font(current_settings.window_height)) #Update all buttons to be proportional to the new resolution.
                    
                    for r in display_box_list:
                        r.resize(current_settings.window_width, current_settings.window_height,scaled_font(current_settings.window_height)) #Update all display boxes to be proportional to the new resolution.
                    
                    logo = pygame.transform.scale(logo, (current_settings.window_width*0.5, current_settings.window_height*0.433))
                    pygame.display.set_caption("BLOCKADE (main menu)")

                elif b == settings_menu_button:
                    current_settings = settings(current_settings)
                    window = pygame.display.set_mode((current_settings.window_width, current_settings.window_height))  
                    for r in button_list:
                        r.resize(current_settings.window_width, current_settings.window_height,scaled_font(current_settings.window_height)) #Update all buttons to be proportional to the new resolution.
                    
                    for r in display_box_list:
                        r.resize(current_settings.window_width, current_settings.window_height,scaled_font(current_settings.window_height)) #Update all display boxes to be proportional to the new resolution.
                    
                    logo = pygame.transform.scale(logo, (current_settings.window_width*0.5, current_settings.window_height*0.433))
                    pygame.display.set_caption("BLOCKADE (main menu)")

                elif b == advice_button:
                    b.text = rand_item(advice_list)
                    b.text_surface = scaled_font(current_settings.window_height).render(b.text,True,WHITE) #When the button is clicked a new random hint / tip is generated.

                elif b == exit_button:
                    sys.exit() #Exit the software if this button is clicked.

        #drawing
        window.blit(background, (0, 0)) #fill in the background
        
        for b in button_list:
            b.b_draw(window) #loop through all of the buttons and draw them onto the window.
        
        for b in display_box_list: #loop through all of the display boxes and draw them onto the window.
            b.b_draw(window)
        

        window.blit(logo, (current_settings.window_width*0.45, current_settings.window_height*0.033)) #placeholder for logo
        
        pygame.display.update() #Updates the frames in the window.