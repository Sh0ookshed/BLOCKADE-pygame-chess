#file for the button class which will be utilised across various parts of my program

#libaries
import pygame

#other file imports
from utils.UI.display_box import Display_box

#initialisation
pygame.init()

#button class
class Button(Display_box):

    #attributes
    def __init__(self,text,window_width,window_height,box_x,box_y,box_w,box_h,font,box_colour,hover_colour,text_colour):
        super().__init__(text,window_width,window_height,box_x,box_y,box_w,box_h,font,box_colour,text_colour)

        #variable attributes
        self.hover_colour = hover_colour
        
        #set attributes
        self.hover = False
        self.clicked = False
        
    #methods    
    def detect_mouse(self,mouse_pos): #method for detecting if the mouse is over the button or not
        self.hover = self.box_rect.collidepoint(mouse_pos)

    def check_for_click(self,events): #method to see if the button has been clicked by the mouse
        self.clicked = False
        for event in events:
            if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1: # 1 is left mouse button in pygame
                if self.hover == True:
                    self.clicked = True
        return self.clicked

    def b_draw(self,window_surface): #method to just draw the button onto the window.
        button_colour = self.box_colour
        if self.hover == True:
            button_colour = self.hover_colour
        pygame.draw.rect(window_surface,button_colour,self.box_rect)
        window_surface.blit(self.text_surface,self.text_surface_rect)