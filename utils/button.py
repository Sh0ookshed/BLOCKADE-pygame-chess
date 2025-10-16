#file for the button class which will be utilised across various parts of my program

#libaries
import pygame

#initialisation
pygame.init()

#button class
class Button:

    #attributes
    def __init__(self,text,window_width,window_height,button_x,button_y,button_w,button_h,font,normal_colour,hover_colour,text_colour):

        #variable attributes
        self.text = text
        self.button_x = button_x
        self.button_y = button_y
        self.button_w = button_w
        self.button_h = button_h
        self.button_rect = pygame.Rect((window_width*button_x,window_height*button_y,window_width*button_w,window_height*button_h))
        self.font = font
        self.normal_colour = normal_colour
        self.hover_colour = hover_colour
        self.text_colour = text_colour

        #set attributes
        self.hover = False
        self.clicked = False
        
        #text that will be on the button + the text rectangle that can blit onto the button rectangle
        self.text_surface = self.font.render(self.text,True, self.text_colour)
        self.text_surface_rect = self.text_surface.get_rect(center = self.button_rect.center)
        
    #methods    
    def detect_mouse(self,mouse_pos): #method for detecting if the mouse is over the button or not
        self.hover = self.button_rect.collidepoint(mouse_pos)

    def check_for_click(self,events): #method to see if the button has been clicked by the mouse
        self.clicked = False
        for event in events:
            if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1: # 1 is left mouse button in pygame
                if self.hover == True:
                    self.clicked = True
        return self.clicked

    def button_draw(self,window_surface): #method to just draw the button onto the window.
        button_colour = self.normal_colour
        if self.hover == True:
            button_colour = self.hover_colour
        pygame.draw.rect(window_surface,button_colour,self.button_rect)
        window_surface.blit(self.text_surface,self.text_surface_rect)

    def resize(self,width,height,font):
        self.button_rect = pygame.Rect((width*self.button_x,height*self.button_y,width*self.button_w,height*self.button_h))
        self.text_surface = font.render(self.text,True, self.text_colour)
        self.text_surface_rect = self.text_surface.get_rect(center = self.button_rect.center)