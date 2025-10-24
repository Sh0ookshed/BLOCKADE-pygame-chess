#------------------------------------------------------------------------------
#SETTINGS WINDOW
#------------------------------------------------------------------------------

#Contains the function for the settings window, this is where the user will change different variables
#such as audio volume, feedback modes, screen resoluion and also time limits on chess clocks.

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
from utils.UI.dropdown import dropdown_button
from resources.colours import *
from resources.dropdown_values import * #Required for any dropdown boxes as this contains the list for the dropdown boxes.

#------------------------------------------------------------------------------
#initialisation
#------------------------------------------------------------------------------
pygame.init()

#------------------------------------------------------------------------------
#settings menu window function
#------------------------------------------------------------------------------
def settings(cw,ch):
    #display configs
    window = pygame.display.set_mode((cw,ch)) #The parameters: cw = Current width, ch = Current height (Referring to the size of the display).
    pygame.display.set_caption("BLOCKADE (settings)") #Allows user to see game name and be clear what window they are in.
    
    #creating display boxes
    resolution_db = Display_box("RESOLUTION:",cw,ch, 0.025, 0.033, 0.4, 0.15,scaled_font(ch),DARKBLUE,WHITE) #Display box that points towards resolution button.

    audio_db = Display_box("AUDIO:",cw,ch, 0.025, 0.213, 0.4, 0.15,scaled_font(ch),DARKBLUE,WHITE) #Display box that points towards audio adjustment buttons.

    audio_display_db = Display_box("(1-100)",cw,ch,0.55,0.213,0.3,0.15,scaled_font(ch),DARKBLUE,WHITE) #Display box that displays the current audio level.

    feedback_db = Display_box("FEEDBACK:",cw,ch, 0.025, 0.393, 0.4, 0.15,scaled_font(ch),DARKBLUE,WHITE) #Display box that points towards the feedback option buttons.

    time_limit_db = Display_box("TIME LIMIT:",cw,ch, 0.025, 0.573, 0.4, 0.15,scaled_font(ch),DARKBLUE,WHITE) #Display box that points towards the time limit button.

    #creating buttons / dropdown buttons
    return_button = Button("return to main menu",cw,ch, 0.225, 0.753, 0.4, 0.15,scaled_font(ch),DARKBLUE,LIGHTBLUE,WHITE) #Returns the user to the main menu

    volume_down_button = Button("<",cw,ch,0.45,0.213,0.1,0.15,scaled_font(ch),DARKBLUE,LIGHTBLUE,WHITE) #Turns the volume down.

    volume_up_button = Button(">",cw,ch,0.85,0.213,0.1,0.15,scaled_font(ch),DARKBLUE,LIGHTBLUE,WHITE) #Turns the volume up.

    f_live = Button("live",cw,ch,0.45,0.393,0.25,0.15,scaled_font(ch),DARKBLUE,LIGHTBLUE,WHITE) #This button when selected turns the gameplay feedback into live mode.

    f_post = Button("post game",cw,ch,0.7,0.393,0.25,0.15,scaled_font(ch),DARKBLUE,LIGHTBLUE,WHITE) #This button when selected turns the gameplay feedback into post game mode.

    resolution_choice = dropdown_button(f"{window.get_size()}",cw,ch, 0.45, 0.033, 0.5, 0.15,scaled_font(ch),DARKBLUE,LIGHTBLUE,WHITE) #Dropdown menu that lets user choose resolution.

    time_choice = dropdown_button("10",cw,ch,0.45,0.573,0.5,0.15,scaled_font(ch),DARKBLUE,LIGHTBLUE,WHITE) #Dropdown menu that lets the user choose the chess clock time.

    #lists for easy management and drawing
    button_list = [return_button, volume_down_button, volume_up_button, resolution_choice,f_live,f_post, time_choice] #Button list lets the program loop through buttons to iteratively draw and interact with them.

    display_box_list = [resolution_db, audio_db, audio_display_db, feedback_db, time_limit_db] #Display box list lets the program loop through display boxes to iteratively draw them.


    #window loop #While the variable "active" is true the win statistics function won't end unless forcefully exited.
    active = True
    while active:
        event_handler = pygame.event.get() #The event handler checks through every single possible pygame event.
        mouse_position = pygame.mouse.get_pos() #Allows the tracking of the mouse position.
        for event in event_handler:
            if event.type == pygame.QUIT:    #If you click on the X in the top right it will exit the software.
                sys.exit()

        for b in button_list: #Loop through every button to give each one a unique function
            if resolution_choice.opened == False and time_choice.opened == False: #This is so that when the dropdown buttons are open the only buttons that can be pressed are the dropdown ones.
                b.detect_mouse(mouse_position)
                b.check_for_click(event_handler)  #Check for where the mouse is and if it has clicked the button.
                if b.clicked == True:
                    if b == return_button:
                        return (cw,ch)
            elif resolution_choice.opened == True: #When resolution choice dropdown is open only the dropdown buttons can be pressed.
                if b == resolution_choice:
                    b.detect_mouse(mouse_position)
                    b.check_for_click(event_handler)
            else:
                if b == time_choice:   #When time choice dropdown is open only the dropdown buttons can be pressed.
                    b.detect_mouse(mouse_position)
                    b.check_for_click(event_handler)


        #drawing
        window.fill((0,0,0)) #fill in the background

        for b in button_list: #loop through all of the buttons and draw them onto the window.
            b.b_draw(window)

        for b in display_box_list: #loop through all of the display boxes and draw them onto the window.
            b.b_draw(window)
        
        if resolution_choice.opened == True:
            chosen_res = resolutions[resolution_choice.drop(resolutions,window,mouse_position,event_handler)] #If the dropdown gets clicked, open the dropdown and when an option is clicked return the index for it.
        
        elif time_choice.opened == True:
            chosen_time = chess_times[time_choice.drop(chess_times,window,mouse_position,event_handler)]

        pygame.display.update() #Updates the frames in the window.

        