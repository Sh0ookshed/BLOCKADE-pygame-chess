#------------------------------------------------------------------------------
#KNIGHT
#------------------------------------------------------------------------------

#knight chess piece class containing all animations and validation + frontend for the knight

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
#knight class
#------------------------------------------------------------------------------
class knight_p(chess_piece):
    def __init__(self, colour, p_ID, square):
        super().__init__(colour, p_ID, square) #stores paramaters the same as the parent class

        #attributes
        self.image = pygame.image.load("assets/general pictures/placeholder.png").convert() #change image to knight image once created
        self.p_value = 3 #how many points the knight is worth