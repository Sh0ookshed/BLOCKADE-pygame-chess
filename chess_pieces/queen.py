#------------------------------------------------------------------------------
#QUEEN
#------------------------------------------------------------------------------

#queen chess piece class containing all animations and validation + frontend for the queen

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
#queen class
#------------------------------------------------------------------------------
class queen_p(chess_piece):
    def __init__(self, colour, p_ID, square):
        super().__init__(colour, p_ID, square)

        #attributes
        self.image = pygame.image.load("assets/general pictures/placeholder.png").convert() #change image to queen image once created
        self.p_value = 9 #how many points the queen is worth