#------------------------------------------------------------------------------
#KING
#------------------------------------------------------------------------------

#king chess piece class containing all animations and validation + frontend for the king

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
#king class
#------------------------------------------------------------------------------
class king_p(chess_piece):
    def __init__(self, p_ID, square, colour, image):
        super().__init__(p_ID, square, colour, image) #stores paramaters the same as the parent class

        #attributes
        self.p_value = 10000 #how many points the king is worth. technically invaluable so a very big number is needed to value it

        #boolean states
        in_check = False #if the king is in check this is set to true