# contains the functions for the multiple end of game windows

#libaries
import pygame
import sys

#initialisation
pygame.init()

#win scenario function
def you_win():
    #display configs
    pygame.display.set_mode((500,500)) #PLACEHOLDER VALUES this will 100% change bc of settings and resizing
    pygame.display.set_caption("chess game (you win!)") #"chess game" is also placeholder until better name
    
    #window loop
    active = True
    while active:
        for event in pygame.event.get():
            if event.type == pygame.QUIT():    #also need to work out how to down the whole program from exit
                active = False

#draw scenario function
def you_draw():
    #display configs
    pygame.display.set_mode((500,500)) #PLACEHOLDER VALUES this will 100% change bc of settings and resizing
    pygame.display.set_caption("chess game (you draw!)") #"chess game" is also placeholder until better name
    
    #window loop
    active = True
    while active:
        for event in pygame.event.get():
            if event.type == pygame.QUIT():    #also need to work out how to down the whole program from exit
                active = False

#lose scenario function
def you_lose():
    #display configs
    pygame.display.set_mode((500,500)) #PLACEHOLDER VALUES this will 100% change bc of settings and resizing
    pygame.display.set_caption("chess game (you lost!)") #"chess game" is also placeholder until better name
    
    #window loop
    active = True
    while active:
        for event in pygame.event.get():
            if event.type == pygame.QUIT():    #also need to work out how to down the whole program from exit
                active = False