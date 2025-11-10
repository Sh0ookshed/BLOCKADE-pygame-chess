#------------------------------------------------------------------------------
#IMAGE BOX
#------------------------------------------------------------------------------

#Class for the image box which is a rectangle that can display images.

#------------------------------------------------------------------------------
#libaries
#------------------------------------------------------------------------------
import pygame #GUI

#------------------------------------------------------------------------------
#initialisation
#------------------------------------------------------------------------------
pygame.init()

#------------------------------------------------------------------------------
#Image box class
#------------------------------------------------------------------------------
class Chess_square:
    
    #attributes
    def __init__(self,image,window_width,window_height,box_x,box_y,box_w,box_h,box_colour):
        

        #variable attributes
        self.window_width = window_width
        self.window_height = window_height
        self.box_x = box_x # All box measurements are just a proportion of the whole window.
        self.box_y = box_y
        self.box_w = box_w
        self.box_h = box_h
        self.box_rect = pygame.Rect((window_width*box_x,window_height*box_y,window_width*box_w,window_height*box_h)) #Creating the rectangle that will contain the text.
        self.box_colour = box_colour

        self.empty = False
        #self.image_surface_rect = self.box_rect.get_rect(center = self.box_rect.center)

        #seeing if it has an image in it or not
        if image == "none":
            self.empty = True
            self.image = image
        else:
            self.image == pygame.image.load(self.image).convert_alpha()
            self.image == pygame.transform.scale(image,self.box_rect.width,self.box_rect.height)
            
        
        
    def draw_box(self,window_surface):
        if self.empty == True:
            pygame.draw.rect(window_surface,self.box_colour,self.box_rect)
        else:
            pygame.draw.rect(window_surface,self.box_colour,self.box_rect)
            window_surface.blit(self.image,self.box_rect)
