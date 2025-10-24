#contains the function for the settings window

#libaries
import pygame
import sys

#other file imports
from utils.scalable_font import scaled_font
from utils.UI.display_box import Display_box
from utils.UI.button import Button
from utils.UI.dropdown import dropdown_button
from resources.colours import *
from resources.dropdown_values import *

#initialisation
pygame.init()


#settings menu window function
def settings(cw,ch):
    #display configs
    window = pygame.display.set_mode((cw,ch)) #PLACEHOLDER VALUES this will 100% change bc of settings and resizing
    pygame.display.set_caption("BLOCKADE (settings)") #allows user to see game name and be clear what window they are in
    
    #creating display boxes
    resolution_db = Display_box("RESOLUTION:",cw,ch, 0.025, 0.033, 0.4, 0.15,scaled_font(ch),DARKBLUE,WHITE)

    audio_db = Display_box("AUDIO:",cw,ch, 0.025, 0.213, 0.4, 0.15,scaled_font(ch),DARKBLUE,WHITE)

    audio_display_db = Display_box("(1-100)",cw,ch,0.55,0.213,0.3,0.15,scaled_font(ch),DARKBLUE,WHITE)

    feedback_db = Display_box("FEEDBACK:",cw,ch, 0.025, 0.393, 0.4, 0.15,scaled_font(ch),DARKBLUE,WHITE)

    time_limit_db = Display_box("TIME LIMIT:",cw,ch, 0.025, 0.573, 0.4, 0.15,scaled_font(ch),DARKBLUE,WHITE)

    #creating buttons / dropdown buttons
    return_button = Button("return to main menu",cw,ch, 0.225, 0.753, 0.4, 0.15,scaled_font(ch),DARKBLUE,LIGHTBLUE,WHITE)

    volume_down_button = Button("<",cw,ch,0.45,0.213,0.1,0.15,scaled_font(ch),DARKBLUE,LIGHTBLUE,WHITE)

    volume_up_button = Button(">",cw,ch,0.85,0.213,0.1,0.15,scaled_font(ch),DARKBLUE,LIGHTBLUE,WHITE)

    f_live = Button("live",cw,ch,0.45,0.393,0.25,0.15,scaled_font(ch),DARKBLUE,LIGHTBLUE,WHITE)

    f_post = Button("post game",cw,ch,0.7,0.393,0.25,0.15,scaled_font(ch),DARKBLUE,LIGHTBLUE,WHITE)

    resolution_choice = dropdown_button(f"{window.get_size()}",cw,ch, 0.45, 0.033, 0.5, 0.15,scaled_font(ch),DARKBLUE,LIGHTBLUE,WHITE)

    time_choice = dropdown_button("10",cw,ch,0.45,0.573,0.5,0.15,scaled_font(ch),DARKBLUE,LIGHTBLUE,WHITE)

    #lists for easy management and drawing
    button_list = [return_button, volume_down_button, volume_up_button, resolution_choice,f_live,f_post, time_choice]

    display_box_list = [resolution_db, audio_db, audio_display_db, feedback_db, time_limit_db]


    #window loop
    active = True
    while active:
        event_handler = pygame.event.get()
        mouse_position = pygame.mouse.get_pos()
        for event in event_handler:
            if event.type == pygame.QUIT:    
                sys.exit()

        for b in button_list:
            if resolution_choice.opened == False and time_choice.opened == False:
                b.detect_mouse(mouse_position)
                b.check_for_click(event_handler)
                if b.clicked == True:
                    if b == return_button:
                        return (cw,ch)
            elif resolution_choice.opened == True:
                if b == resolution_choice:
                    b.detect_mouse(mouse_position)
                    b.check_for_click(event_handler)
            else:
                if b == time_choice:
                    b.detect_mouse(mouse_position)
                    b.check_for_click(event_handler)


        #drawing
        window.fill((0,0,0))

        for b in button_list:
            b.b_draw(window)

        for b in display_box_list:
            b.b_draw(window)
        
        if resolution_choice.opened == True:
            chosen_res = resolutions[resolution_choice.drop(resolutions,window,mouse_position,event_handler)]
        
        elif time_choice.opened == True:
            chosen_time = chess_times[time_choice.drop(chess_times,window,mouse_position,event_handler)]

        pygame.display.update()

        