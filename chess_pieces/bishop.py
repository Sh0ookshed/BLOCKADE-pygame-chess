#------------------------------------------------------------------------------
#BISHOP
#------------------------------------------------------------------------------

#bishop chess piece class containing all animations and validation + frontend for bishop

#------------------------------------------------------------------------------
#libraries
#------------------------------------------------------------------------------
import pygame #GUI

#------------------------------------------------------------------------------
#initialisation
#------------------------------------------------------------------------------
pygame.init()

#------------------------------------------------------------------------------
#file imports
#------------------------------------------------------------------------------
from _chess_piece import chess_piece

#------------------------------------------------------------------------------
#bishop class
#------------------------------------------------------------------------------
class bishop_p(chess_piece):
    def __init__(self, colour, p_ID, square):
        super().__init__(colour, p_ID, square) #stores paramaters the same as the parent class

        #attributes
        self.image = pygame.image.load("assets/general pictures/placeholder.png").convert() #change image to bishop image once created
        self.p_value = 3 #how many points the bishop is worth