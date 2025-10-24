#class for the display box which is a rectangle that can display text

#libaries
import pygame

#initialisation
pygame.init()

#button class
class Display_box:

    #attributes
    def __init__(self,text,window_width,window_height,box_x,box_y,box_w,box_h,font,box_colour,text_colour):

        #variable attributes
        self.text = text
        self.window_width = window_width
        self.window_height = window_height
        self.box_x = box_x
        self.box_y = box_y
        self.box_w = box_w
        self.box_h = box_h
        self.box_rect = pygame.Rect((window_width*box_x,window_height*box_y,window_width*box_w,window_height*box_h))
        self.font = font
        self.box_colour = box_colour
        self.text_colour = text_colour

        #text that will be on the button + the text rectangle that can blit onto the button rectangle
        self.text_surface = self.font.render(self.text,True, self.text_colour)
        self.text_surface_rect = self.text_surface.get_rect(center = self.box_rect.center)
        
    #methods    

    def b_draw(self,window_surface): #method to just draw the button onto the window.
        pygame.draw.rect(window_surface,self.box_colour,self.box_rect)
        window_surface.blit(self.text_surface,self.text_surface_rect)

    def resize(self,width,height,font):
        self.box_rect = pygame.Rect((width*self.box_x,height*self.box_y,width*self.box_w,height*self.box_h))
        self.text_surface = font.render(self.text,True, self.text_colour)
        self.text_surface_rect = self.text_surface.get_rect(center = self.box_rect.center)