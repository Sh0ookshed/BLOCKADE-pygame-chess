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
def create_chess_board(width,height,cream,grey):  #creates an 8x8 grid of chess squares to represent the chess board with the colouring the same as a real life chess board.
    chess_board = []
    box_y = 0

    for create in range (8): #creating rows
        row = []
        box_x = 0

        for r in range(8): #creating squares within the rows to create an 8x8

            if create % 2 == 0:

                if r % 2 == 0:
                    row.append(Chess_square("none",width,height,box_x,box_y,0.125,0.125,cream)) #cream because otherwise white pieces will be invisible ontop of it
                    box_x += 0.125

                else:
                    row.append(Chess_square("none",width,height,box_x,box_y,0.125,0.125,grey)) #grey because otherwise black pieces will be invisible ontop of it
                    box_x += 0.125

            else:

                if r % 2 == 0:
                    row.append(Chess_square("none",width,height,box_x,box_y,0.125,0.125,grey))
                    box_x += 0.125

                else:
                    row.append(Chess_square("none",width,height,box_x,box_y,0.125,0.125,cream))
                    box_x += 0.125

        chess_board.append(row)
        box_y += 0.125
    return chess_board #returns the list that holds all the row sublists which hold all the squares