#this file contains the function / variable for the scalable font that changes size based on resolution

#libraries
import pygame

#initialisation
pygame.init()

#function for making sure the font is a proportional size to window
def scaled_font(height):
    font = pygame.font.Font(None,int(height*0.08))
    return font