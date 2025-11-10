#------------------------------------------------------------------------------
#CHESS BOARD
#------------------------------------------------------------------------------

#This file contains the function for the chess board. This is purely UI and will render the chess board onto the
#screen which then can have pieces rendered ontop of it seperately

#------------------------------------------------------------------------------
#libaries
#------------------------------------------------------------------------------
import pygame

#------------------------------------------------------------------------------
#File imports
#------------------------------------------------------------------------------
from utils.UI.chess_UI.chess_square import Chess_square

#------------------------------------------------------------------------------
#initialisation
#------------------------------------------------------------------------------
pygame.init()

#------------------------------------------------------------------------------
#draw_chess_board function
#------------------------------------------------------------------------------
def create_chess_board(width,height,white,grey):
    chess_board = []
    box_y = 0
    for create in range (8):
        row = []
        box_x = 0
        for r in range(8):
            if create % 2 == 0:
                if r % 2 == 0:
                    row.append(Chess_square("none",width,height,box_x,box_y,0.125,0.125,white))
                    box_x += 0.125
                else:
                    row.append(Chess_square("none",width,height,box_x,box_y,0.125,0.125,grey))
                    box_x += 0.125
            else:
                if r % 2 == 0:
                    row.append(Chess_square("none",width,height,box_x,box_y,0.125,0.125,grey))
                    box_x += 0.125
                else:
                    row.append(Chess_square("none",width,height,box_x,box_y,0.125,0.125,white))
                    box_x += 0.125
        chess_board.append(row)
        box_y += 0.125
    return chess_board