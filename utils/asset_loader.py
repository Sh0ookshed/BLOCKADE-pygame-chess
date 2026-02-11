#------------------------------------------------------------------------------
#ASSET LOADER
#------------------------------------------------------------------------------

#loads assets on the main file to keep performance high once the program has loaded

#------------------------------------------------------------------------------
#libraries
#------------------------------------------------------------------------------
import pygame #GUI

#------------------------------------------------------------------------------
#initialisation
#------------------------------------------------------------------------------
pygame.init()

#------------------------------------------------------------------------------
#asset loader function
#------------------------------------------------------------------------------
class asset_load:
    
    def __init__(self):
        #misc assets
        self.placeholder_image = pygame.image.load("assets/general pictures/placeholder.png").convert()
        
        #black chess piece assets
        self.black_bishop_image = pygame.image.load("assets/chess_piece_pictures/black bishop.png").convert()
        self.black_king_image = pygame.image.load("assets/chess_piece_pictures/black king.png").convert()
        self.black_knight_image = pygame.image.load("assets/chess_piece_pictures/black knight.png").convert()
        self.black_pawn_image = pygame.image.load("assets/chess_piece_pictures/black pawn.png").convert()
        self.black_queen_image = pygame.image.load("assets/chess_piece_pictures/black queen.png").convert()
        self.black_rook_image = pygame.image.load("assets/chess_piece_pictures/black rook.png").convert()
        
        #white chess piece assets
        self.white_bishop_image = pygame.image.load("assets/chess_piece_pictures/white bishop.png").convert()
        self.white_king_image = pygame.image.load("assets/chess_piece_pictures/white king.png").convert()
        self.white_knight_image = pygame.image.load("assets/chess_piece_pictures/white knight.png").convert()
        self.white_pawn_image = pygame.image.load("assets/chess_piece_pictures/white pawn.png").convert()
        self.white_queen_image = pygame.image.load("assets/chess_piece_pictures/white queen.png").convert()
        self.white_rook_image = pygame.image.load("assets/chess_piece_pictures/white rook.png").convert()