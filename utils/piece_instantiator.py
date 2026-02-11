#------------------------------------------------------------------------------
#PIECE INSTANTIATOR
#------------------------------------------------------------------------------

#The piece instantiator, as in the name instantiates all of the pieces into objects for both the algorithm to use and the user to use
#it creates both a list of white piece objects and black piece objects. It gives each piece their own colour. piece ID and appropriate image

#------------------------------------------------------------------------------
#libraries
#------------------------------------------------------------------------------
import pygame #GUI

#------------------------------------------------------------------------------
#file imports
#------------------------------------------------------------------------------
from chess_pieces.bishop import bishop_p 
from chess_pieces.king import king_p
from chess_pieces.knight import knight_p
from chess_pieces.pawn import pawn_p
from chess_pieces.queen import queen_p
from chess_pieces.rook import rook_p

#------------------------------------------------------------------------------
#initialisation
#------------------------------------------------------------------------------
pygame.init()

#------------------------------------------------------------------------------
#Chess piece class
#------------------------------------------------------------------------------

#placeholder
placeholder_image = pygame.image.load("assets/general pictures/placeholder.png").convert() #will change one chess piece assets are completed

def Piece_instantiator(chess_square, black, white):
    black_piece_list = []
    white_piece_list = []

    for i in range(8): #pawns

        black_piece_list.append(pawn_p(("b",101+i), chess_square, black, placeholder_image))
        white_piece_list.append(pawn_p(("w",101+i), chess_square, white, placeholder_image))

    for i in range(2): #knights, bishops and rooks
        
        black_piece_list.append(knight_p((f"b",201+i), chess_square, black, placeholder_image))
        white_piece_list.append(knight_p(("w",201+i), chess_square, white, placeholder_image))

        black_piece_list.append(bishop_p(("b",301+i), chess_square, black, placeholder_image))
        white_piece_list.append(bishop_p(("w",301+i), chess_square, white, placeholder_image))

        black_piece_list.append(rook_p(("b",401+i), chess_square, black, placeholder_image))
        white_piece_list.append(rook_p(("w",401+i), chess_square, white, placeholder_image))
    
    #queens
    black_piece_list.append(queen_p(("b",501), chess_square, black, placeholder_image))
    white_piece_list.append(queen_p(("w",501), chess_square, white, placeholder_image))

    #kings
    black_piece_list.append(king_p(("b",601), chess_square, black, placeholder_image))
    white_piece_list.append(king_p(("w",601), chess_square, white, placeholder_image))

    return (black_piece_list,white_piece_list) #returns both lists as a tuple 