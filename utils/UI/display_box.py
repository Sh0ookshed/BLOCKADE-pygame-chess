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
#File imports
#------------------------------------------------------------------------------
from utils.text_wrapper import text_wrap

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
        self.text_lines = text_wrap(self.text, self.font, self.box_w*self.window_width)

    #methods    

    def b_draw(self,window_surface): #Method to draw the display box onto the window.
        pygame.draw.rect(window_surface,self.box_colour,self.box_rect)
        text_size_total = sum(self.font.size(line)[1] for line in self.text_lines)

        line_position = (self.window_height*self.box_y) + (self.box_h*self.window_height - text_size_total) / 2

        for line in self.text_lines:
            text_surface = self.font.render(line,True,self.text_colour)

            x_centre = (self.box_x*self.window_width) + ((self.box_w*self.window_width) / 2)

            window_surface.blit(text_surface, ((x_centre - (text_surface.get_width() / 2)), line_position))
            line_position += text_surface.get_height()


    def resize(self,width,height,font): #Method to resize the display box so that it is still proportional with the screen. 
        self.box_rect = pygame.Rect((width*self.box_x,height*self.box_y,width*self.box_w,height*self.box_h))
        self.text_lines = text_wrap(self.text, font, self.box_w*width)
        self.font = font
        self.window_width = width
        self.window_height = height
