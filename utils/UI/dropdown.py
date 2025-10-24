#file for the dropdown class which will be a dropdown button menu that will be used within my settings menu

#libaries
import pygame
import sys

#other file imports
from utils.UI.button import Button

#initialisation
pygame.init()

#dropdown button class
class dropdown_button(Button):
    def __init__(self, text, window_width, window_height, box_x, box_y, box_w, box_h, font, box_colour, hover_colour, text_colour):
        super().__init__(text, window_width, window_height, box_x, box_y, box_w, box_h, font, box_colour, hover_colour, text_colour)

        #variable attributes
        self.open_text = self.text+"<"
        self.close_text = self.text+">"
        self.text_surface = self.font.render(self.close_text,True, self.text_colour)
        self.text_surface_rect = self.text_surface.get_rect(center = self.box_rect.center)

        #set attributes
        self.opened = False






    def check_for_click(self,events): #method to see if the button has been clicked by the mouse
        self.clicked = False
        for event in events:
            if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1: # 1 is left mouse button in pygame
                if self.hover == True and self.opened ==True:
                    self.clicked = True
                    self.opened = False
                    self.text_surface = self.font.render(self.close_text,True, self.text_colour)
                    self.text_surface_rect = self.text_surface.get_rect(center = self.box_rect.center)
                    return self.clicked, self.opened

                elif self.hover == True:
                    self.clicked = True
                    self.opened = True
                    self.text_surface = self.font.render(self.open_text,True, self.text_colour)
                    self.text_surface_rect = self.text_surface.get_rect(center = self.box_rect.center)
                    return self.clicked, self.opened





    def drop(self,dropdown_list,window_surface,mouse_pos,events):
        current_y= self.box_y
        dropbox_list = []
        current_option = self.text
        self.open_text = self.text+"<"
        self.close_text = self.text+">"

        if self.window_height > (self.box_y*self.window_height) + (self.box_h*self.window_height) + (self.box_h*0.5*len(dropdown_list)*self.window_height):

            for x, option in enumerate(dropdown_list):
                if str(option) == str(current_option):
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

        for n, d in enumerate(dropbox_list):
            d.detect_mouse(mouse_pos)
            d.check_for_click(events)
            d.b_draw(window_surface)

            if d.clicked == True:
                self.text = str(dropdown_list[n])
                self.close_text = self.text+">"
                self.open_text = self.text+"<"
                self.text_surface = self.font.render(self.close_text,True, self.text_colour)
                self.text_surface_rect = self.text_surface.get_rect(center = self.box_rect.center)
                self.opened = False
                chosen_index = n

        return chosen_index