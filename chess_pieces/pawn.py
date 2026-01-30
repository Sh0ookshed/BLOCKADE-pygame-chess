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
    def __init__(self, p_ID, square, colour, image):
        super().__init__(p_ID, square, colour, image)

        #attributes
        self.p_value = 1 #how many points the pawn is worth

        #boolean state attributes
        self.promoted = False #for if the pawn gets promoted by reaching the end
        self.moved = False #so the pawn can move 2 squares on the first turn