#------------------------------------------------------------------------------
#DISPLAY BOX
#------------------------------------------------------------------------------

#Class for the display box which is a rectangle that can display text. It will be used to just signpost different
#things in this software.

#------------------------------------------------------------------------------
#libaries
#------------------------------------------------------------------------------
import pygame #GUI

#------------------------------------------------------------------------------
#initialisation
#------------------------------------------------------------------------------
pygame.init()

#------------------------------------------------------------------------------
#Display box class
#------------------------------------------------------------------------------
class Display_box:

    #attributes
    def __init__(self,text,window_width,window_height,box_x,box_y,box_w,box_h,font,box_colour,text_colour): #All parameters that need to be entered.

        #variable attributes
        self.text = text
        self.window_width = window_width
        self.window_height = window_height
        self.box_x = box_x # All box measurements are just a proportion of the whole window.
        self.box_y = box_y
        self.box_w = box_w
        self.box_h = box_h
        self.box_rect = pygame.Rect((window_width*box_x,window_height*box_y,window_width*box_w,window_height*box_h)) #Creating the rectangle that will contain the text.
        self.font = font
        self.box_colour = box_colour
        self.text_colour = text_colour

        #The text that will be on the button and the text rectangle that can blit onto the button rectangle
        self.text_surface = self.font.render(self.text,True, self.text_colour)
        self.text_surface_rect = self.text_surface.get_rect(center = self.box_rect.center)
        
    #methods    

    def b_draw(self,window_surface): #Method to draw the display box onto the window.
        pygame.draw.rect(window_surface,self.box_colour,self.box_rect)
        window_surface.blit(self.text_surface,self.text_surface_rect)

    def resize(self,width,height,font): #Method to resize the display box so that it is still proportional with the screen. 
        self.box_rect = pygame.Rect((width*self.box_x,height*self.box_y,width*self.box_w,height*self.box_h))
        self.text_surface = font.render(self.text,True, self.text_colour)
        self.text_surface_rect = self.text_surface.get_rect(center = self.box_rect.center)