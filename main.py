#from update import update_board
from board import chessboard_class
from draw import init_board, draw_board        

STARTING_BOARD = "rnbqkbnr/pppppppp/8/8/8/8/PPPPPPPP/RNBQKBNR w KQkq - 0 1"

if __name__ == "__main__":

    screen = init_board() #this draws the board
    main_board = chessboard_class()
    main_board.read_FEN(STARTING_BOARD)

    #main game loop
    while (True): 
        #update_board(main_board)
        draw_board(main_board, screen) 
        a = input()