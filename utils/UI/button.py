#------------------------------------------------------------------------------
#BUTTON
#------------------------------------------------------------------------------

#Class for the button which will be used for numerous things in my softwre but mainly to either change settings
#or move from one window to another or to exit the program entirely.

#------------------------------------------------------------------------------
#libaries
#------------------------------------------------------------------------------
import pygame #GUI

#------------------------------------------------------------------------------
#File imports
#------------------------------------------------------------------------------
from utils.UI.display_box import Display_box #Button inherits from Display box

from utils.text_wrapper import text_wrap

#------------------------------------------------------------------------------
#initialisation
#------------------------------------------------------------------------------
pygame.init()

#------------------------------------------------------------------------------
#button class
#------------------------------------------------------------------------------
class Button(Display_box):

    #attributes
    def __init__(self,text,window_width,window_height,box_x,box_y,box_w,box_h,font,box_colour,hover_colour,text_colour): #All parameters that need to be entered.
        super().__init__(text,window_width,window_height,box_x,box_y,box_w,box_h,font,box_colour,text_colour) #Parameters that inherit from parent class (Display box).

        #variable attributes
        self.hover_colour = hover_colour
        
        #set attributes
        self.hover = False
        self.clicked = False
        
    #methods    
    def detect_mouse(self,mouse_pos): #Method for detecting if the mouse is hovering over the button or not.
        self.hover = self.box_rect.collidepoint(mouse_pos)

    def check_for_click(self,events): #Method to see if the button has been clicked by the mouse or not.
        self.clicked = False
        for event in events:
            if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1: # 1 is left mouse button in pygame.
                if self.hover == True:
                    self.clicked = True
        return self.clicked

    def b_draw(self,window_surface): #Method to draw the button onto the window (slightly edited from Display box version due to extra functionality).
        button_colour = self.box_colour
        if self.hover == True:
            button_colour = self.hover_colour

        pygame.draw.rect(window_surface,button_colour,self.box_rect)
        text_size_total = sum(self.font.size(line)[1] for line in self.text_lines)

        line_position = (self.window_height*self.box_y) + (self.box_h*self.window_height - text_size_total) / 2
        
        for line in self.text_lines:
            text_surface = self.font.render(line,True,self.text_colour)
            
            x_centre = (self.box_x*self.window_width) + ((self.box_w*self.window_width) / 2)

            window_surface.blit(text_surface, ((x_centre - (text_surface.get_width() / 2)), line_position))
            line_position += text_surface.get_height()