#------------------------------------------------------------------------------
#PAWN
#------------------------------------------------------------------------------

#pawn chess piece class containing all animations and validation + frontend for the pawn

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
#pawn class
#------------------------------------------------------------------------------
class pawn_p(chess_piece):
    def __init__(self, colour, p_ID, square):
        super().__init__(colour, p_ID, square)

        #attributes
        self.image = pygame.image.load("assets/general pictures/placeholder.png").convert() #change image to pawn image once created
        self.p_value = 1 #how many points the pawn is worth