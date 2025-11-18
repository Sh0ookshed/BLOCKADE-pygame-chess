#------------------------------------------------------------------------------
#ROOK
#------------------------------------------------------------------------------

#rook chess piece class containing all animations and validation + frontend for the rook

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
#rook class
#------------------------------------------------------------------------------
class rook_p(chess_piece):
    def __init__(self, colour, p_ID, square):
        super().__init__(colour, p_ID, square)

        #attributes
        self.image = pygame.image.load("assets/general pictures/placeholder.png").convert() #change image to rook image once created
        self.p_value = 5 #how many points the rook is worth