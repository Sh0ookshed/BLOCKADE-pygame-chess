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
    def __init__(self, colour, p_ID, square):
        super().__init__(colour, p_ID, square) #stores paramaters the same as the parent class

        #attributes
        self.image = pygame.image.load("assets/general pictures/placeholder.png").convert() #change image to king image once created
        self.p_value = 10000 #how many points the king is worth. technically invaluable so a very big number is needed to value it