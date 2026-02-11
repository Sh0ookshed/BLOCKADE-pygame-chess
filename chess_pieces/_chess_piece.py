#------------------------------------------------------------------------------
#CHESS PIECE
#------------------------------------------------------------------------------

#file containing the parent class for all chess pieces. this creates all of the attributes that can be individualised for each child chess piece

#------------------------------------------------------------------------------
#libraries
#------------------------------------------------------------------------------
import pygame #GUI

#------------------------------------------------------------------------------
#initialisation
#------------------------------------------------------------------------------
pygame.init()

#------------------------------------------------------------------------------
#Chess piece class
#------------------------------------------------------------------------------
class chess_piece:
    
    def __init__(self, p_ID, square, colour, image):

        #attributes
        self.image = pygame.transform.scale(self.image, (self.width*0.9, self.height*0.9)) #image initialisation, make the chess pieces a tiny bit smaller than the square
        self.p_value = 0 #how much the chess piece is worth (for weighting). base value is 0 but will be different for all the child pieces
        
        #variable attributes
        self.width, self.height = square.size #gets the size of the chess square so the piece can scale to fit it
        self.colour = colour
        self.image = image
        self.p_ID = p_ID #p_ID is the piece ID. its used to identify different pieces for the algorithm to understand. IS A TUPLE

        #list attributes for the chess piece
        self.position = [] #coordinates for the chess piece
        self.position_history = [] #history of where the piece has moved
        self.legal_moves = [] #list of legal moves that the piece can make
        self.defending = [] #list of pieces the piece is defending
        self.attacking = [] #list of pieces the piece is attacking
        self.defended_by = [] #list of pieces the piece is being defended by
        self.attacked_by = [] #list of pieces the piece is being attacked by
        
        #boolean state attributes
        self.captured = False
        self.pinned = False