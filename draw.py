import utils
import pygame
from board import chessboard_class

#sizes
DISPLAY_HEIGHT = 640
DISPLAY_WIDTH = 640
BOARD_SIZE = 8
SQUARE_SIZE = DISPLAY_WIDTH//BOARD_SIZE

#colors
DARK_SQUARES = (77, 41, 15)
WHITE_SQUARES = (180, 142, 80)
COLORS = [WHITE_SQUARES, DARK_SQUARES]

def init_board() -> pygame.surface.Surface:
    """
    inits the screen and draws the basic chess pattern, so there is no need to redraw it every time"""
    pygame.init()   
    screen = pygame.display.set_mode((DISPLAY_WIDTH, DISPLAY_HEIGHT))

    #draws the chess pattern, without pieces
    for i in range(BOARD_SIZE):
        for j in range(BOARD_SIZE):
            pygame.draw.rect(screen, COLORS[(j+i)%2], (
                            (i*SQUARE_SIZE, j*SQUARE_SIZE), (SQUARE_SIZE, SQUARE_SIZE)))

    return screen

def draw_board(chessboard: chessboard_class, screen: pygame.surface.Surface) -> None:
    
    for i in range(BOARD_SIZE):
        for j in range(BOARD_SIZE):
            if chessboard.board[i][j] != '-':
                image = pygame.image.load(f"pieces/{chessboard.board[i][j]}.svg")
                scaled_image = pygame.transform.scale(image, (SQUARE_SIZE, SQUARE_SIZE))
                rect_position = pygame.Rect(j*SQUARE_SIZE, (7-i)*SQUARE_SIZE, 
                                            SQUARE_SIZE, SQUARE_SIZE)
                pygame.Surface.blit(screen, scaled_image, rect_position)
    
    pygame.display.flip()