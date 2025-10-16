#contains the function for the main menu window

#libaries
import pygame
import sys

#other file imports
from windows.gameplay_window import gameplay
from windows.settings_window import settings
from windows.win_statistics_window import win_stats
from utils.scalable_font import scaled_font
from utils.button import Button
from utils.random_pick import rand_item
from resources.colours import *
from resources.chess_tips import advice_list

#initialisation
pygame.init()

#main menu window function
def main_menu(cw,ch):

    #display configs
    window = pygame.display.set_mode((cw,ch)) #PLACEHOLDER VALUES this will 100% change bc of settings and resizing

    pygame.display.set_caption("BLOCKADE (main menu)") #allows user to see game name and be clear what window they are in

    #creating buttons
    play_button = Button("play",cw,ch, 0.025, 0.033, 0.4, 0.2,scaled_font(ch),DARKBLUE,LIGHTBLUE,WHITE)

    win_stats_button = Button("view win statistics",cw,ch, 0.025, 0.266, 0.4, 0.2,scaled_font(ch),DARKBLUE,LIGHTBLUE,WHITE)

    settings_menu_button = Button("settings",cw,ch, 0.025, 0.499, 0.4, 0.2,scaled_font(ch),DARKBLUE,LIGHTBLUE,WHITE)

    exit_button = Button("exit",cw,ch, 0.025, 0.732, 0.4, 0.2,scaled_font(ch),DARKBLUE,LIGHTBLUE,WHITE)

    advice_button = Button(rand_item(advice_list),cw,ch, 0.45, 0.499 ,0.5, 0.433,scaled_font(ch),DARKBLUE,LIGHTBLUE,WHITE)

    logo_placeholder = Button("LOGO GOES HERE",cw,ch, 0.45, 0.033, 0.5, 0.433,scaled_font(ch),DARKBLUE,DARKBLUE,WHITE)

    #creating list of buttons
    button_list = [play_button,win_stats_button,settings_menu_button,exit_button,advice_button,logo_placeholder]

    #window loop
    active = True
    while active:
        event_handler = pygame.event.get()
        mouse_position = pygame.mouse.get_pos()

        for event in event_handler:
            if event.type == pygame.QUIT:    
                sys.exit()
        
        for b in button_list:     #note to self this actually works
            b.detect_mouse(mouse_position)
            b.check_for_click(event_handler)
            if b.clicked == True:

                if b == play_button:
                    window = pygame.display.set_mode(gameplay(cw,ch))
                    cw = pygame.display.get_surface().get_width()
                    ch = pygame.display.get_surface().get_height()
                    for r in button_list:
                        r.resize(cw,ch,scaled_font(ch))
                    pygame.display.set_caption("BLOCKADE (main menu)")

                elif b == win_stats_button:
                    window = pygame.display.set_mode(win_stats(cw,ch))
                    cw = pygame.display.get_surface().get_width()
                    ch = pygame.display.get_surface().get_height()
                    for r in button_list:
                        r.resize(cw,ch,scaled_font(ch))
                    pygame.display.set_caption("BLOCKADE (main menu)")

                elif b == settings_menu_button:
                    window = pygame.display.set_mode(settings(cw,ch))
                    cw = pygame.display.get_surface().get_width()
                    ch = pygame.display.get_surface().get_height()
                    for r in button_list:
                        r.resize(cw,ch,scaled_font(ch))
                    pygame.display.set_caption("BLOCKADE (main menu)")

                elif b == advice_button:
                    b.text = rand_item(advice_list)
                    b.text_surface = scaled_font(ch).render(b.text,True,WHITE)

                elif b == exit_button:
                    sys.exit()

        #drawing
        window.fill((0,0,0))
        for b in button_list:
            b.button_draw(window)
        
        pygame.display.update()