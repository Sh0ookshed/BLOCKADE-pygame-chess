#------------------------------------------------------------------------------
#DROPDOWN
#------------------------------------------------------------------------------

#file for the dropdown button class which will be a dropdown button menu that will be used within the settings menu
#and possibly other things within the software.

#------------------------------------------------------------------------------
#libaries
#------------------------------------------------------------------------------
import pygame #GUI
import sys #Clean shutdown

#------------------------------------------------------------------------------
#File imports
#------------------------------------------------------------------------------
from utils.text_wrapper import text_wrap

from utils.UI.button import Button

#------------------------------------------------------------------------------
#initialisation
#------------------------------------------------------------------------------
pygame.init()

#------------------------------------------------------------------------------
#dropdown button class
#------------------------------------------------------------------------------

class dropdown_button(Button):
    def __init__(self, text, window_width, window_height, box_x, box_y, box_w, box_h, font, box_colour, hover_colour, text_colour): #All parameters that need to be entered.
        super().__init__(text, window_width, window_height, box_x, box_y, box_w, box_h, font, box_colour, hover_colour, text_colour) #Parameters that inherit from parent class (Button).

        #variable attributes
        self.open_text = self.text+"<"
        self.close_text = self.text+">"
        self.text_lines = text_wrap(self.close_text, font, self.box_w*self.window_width)

        #set attributes
        self.opened = False


    #methods
    def check_for_click(self,events): #Method to see if the button has been clicked by the mouse edited to now control whether the dropdown is open or not.
        self.clicked = False
        for event in events:
            if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1: # 1 is left mouse button in pygame.
                if self.hover == True and self.opened ==True:   #Closes the dropdown if it is open.
                    self.clicked = True
                    self.opened = False
                    self.text_lines = text_wrap(self.close_text, self.font, self.box_w*self.window_width)
                    return self.clicked, self.opened

                elif self.hover == True: #Opens the dropdown if it is closed
                    self.clicked = True
                    self.opened = True
                    self.text_lines = text_wrap(self.open_text, self.font, self.box_w*self.window_width)
                    return self.clicked, self.opened


    def drop(self,dropdown_list,window_surface,mouse_pos,events): #This method is the actual method that creates the dropdown menu.
        current_y= self.box_y
        dropbox_list = []
        current_option = self.text
        self.open_text = self.text+"<"
        self.close_text = self.text+">"

        if self.window_height > (self.box_y*self.window_height) + (self.box_h*self.window_height) + (self.box_h*0.5*len(dropdown_list)*self.window_height): #Checks if the dropdown menu has enough room below it. If it doesnt it attempts to use the space above it

            for x, option in enumerate(dropdown_list):
                if str(option) == str(current_option): #If the current choice in the dropdown is the same as the selected choice then it will say (current) next to it.
                    chosen_index = x
                    dropbox_list.append(Button(f"{option} (current)", self.window_width,self.window_height, self.box_x, current_y+self.box_h, self.box_w, self.box_h/2, self.font, self.box_colour, self.hover_colour, self.text_colour))
                    current_y += (self.box_h/2)
                else:
                    dropbox_list.append(Button(f"{option}", self.window_width,self.window_height, self.box_x, current_y+self.box_h, self.box_w, self.box_h/2, self.font, self.box_colour, self.hover_colour, self.text_colour))
                    current_y += (self.box_h/2)

        else:

            for x, option in enumerate(dropdown_list):
                if str(option) == str(current_option):
                    chosen_index = x
                    dropbox_list.append(Button(f"{option} (current)", self.window_width,self.window_height, self.box_x, current_y-(self.box_h/2), self.box_w, self.box_h/2, self.font, self.box_colour, self.hover_colour, self.text_colour))
                    current_y -=(self.box_h/2)  
                else:
                    dropbox_list.append(Button(f"{option}", self.window_width,self.window_height, self.box_x, current_y-(self.box_h/2), self.box_w, self.box_h/2, self.font, self.box_colour, self.hover_colour, self.text_colour))
                    current_y -=(self.box_h/2)

        for n, d in enumerate(dropbox_list): #Allows individual dropdown boxes (that are created when the main box is clicked) to be able to be clicked and respond to the mouse.
            d.detect_mouse(mouse_pos)
            d.check_for_click(events)
            d.b_draw(window_surface)

            if d.clicked == True:
                self.text = str(dropdown_list[n])
                self.close_text = self.text+">"       #> Means the dropdown is closed and < means the dropdown is open
                self.open_text = self.text+"<"
                self.text_lines = text_wrap(self.close_text, self.font, self.box_w*self.window_width)
                self.opened = False
                chosen_index = n

        return chosen_index #Returns the index of the chosen dropdown option. This means that the value in the original list that links to the chosen index can be chosen and therefore be used for a functionality such as choosing an new chess clock time or resolution.


    def resize(self,width,height,font): #Method to resize the display box so that it is still proportional with the screen (needs to be redone for dropdown because of open and close text). 
        self.box_rect = pygame.Rect((width*self.box_x,height*self.box_y,width*self.box_w,height*self.box_h))
        self.text_lines = text_wrap(self.close_text, font, self.box_w*width)
        self.font = font
        self.window_width = width
        self.window_height = height