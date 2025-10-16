#contains the function for the settings window

#libaries
import pygame
import sys

#other file imports
from utils.scalable_font import scaled_font
from utils.button import Button
from resources.colours import *

#initialisation
pygame.init()


#settings menu window function
def settings(cw,ch):
    #display configs
    window = pygame.display.set_mode((cw,ch)) #PLACEHOLDER VALUES this will 100% change bc of settings and resizing
    pygame.display.set_caption("BLOCKADE (settings)") #allows user to see game name and be clear what window they are in
    
    #creating buttons
    return_button = Button("return to main menu",cw,ch, 0.4, 0.4, 0.2, 0.1,scaled_font(ch),DARKBLUE,LIGHTBLUE,WHITE)

    test_bigger = Button("BIGGER",cw,ch, 0.4, 0.65, 0.2, 0.1,scaled_font(ch),DARKBLUE,LIGHTBLUE,WHITE)

    test_smaller = Button("SMALLER",cw,ch, 0.4, 0.9, 0.2, 0.1,scaled_font(ch),DARKBLUE,LIGHTBLUE,WHITE)


    button_list = [return_button,test_bigger,test_smaller]

    #window loop
    active = True
    while active:
        event_handler = pygame.event.get()
        mouse_position = pygame.mouse.get_pos()
        for event in event_handler:
            if event.type == pygame.QUIT:    
                sys.exit()
        
        for b in button_list:
            b.detect_mouse(mouse_position)
            b.check_for_click(event_handler)
            if b.clicked == True:
                if b == return_button:
                    return (cw,ch)
                elif b == test_bigger:
                    cw += 20
                    ch += 20
                    window = pygame.display.set_mode((cw,ch))
                    for r in button_list:
                        r.resize(cw,ch,scaled_font(ch))
                elif b == test_smaller:
                    cw -= 20
                    ch -= 20
                    window = pygame.display.set_mode((cw,ch))
                    for r in button_list:
                        r.resize(cw,ch,scaled_font(ch))

        #drawing
        window.fill((0,0,0))

        for b in button_list:
            b.button_draw(window)

        pygame.display.update()

        