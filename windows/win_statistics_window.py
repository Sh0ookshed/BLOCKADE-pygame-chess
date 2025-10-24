#contains the function for the win statistics window

#libaries
import pygame
import sys

#other file imports
from utils.scalable_font import scaled_font
from utils.UI.button import Button
from resources.colours import *

#initialisation
pygame.init()

#win statistics window function
def win_stats(cw,ch):
    #display configs
    window = pygame.display.set_mode((cw,ch)) #PLACEHOLDER VALUES this will 100% change bc of settings and resizing
    pygame.display.set_caption("BLOCKADE (win statistics)") #allows user to see game name and be clear what window they are in
    
    #creating buttons
    return_button = Button("return to main menu",cw,ch, 0.4, 0.4, 0.2, 0.2,scaled_font(ch),DARKBLUE,LIGHTBLUE,WHITE)

    button_list = [return_button]

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
            
        #drawing
        window.fill((0,0,0))
        for b in button_list:
            b.b_draw(window)

        pygame.display.update()