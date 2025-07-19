#from update import update_board
from move import get_move, move_class
from board import Chessboard
from draw import init_board, draw_board        

STARTING_BOARD = "rnbqkbnr/pppppppp/8/8/8/8/PPPPPPPP/RNBQKBNR w KQkq - 0 1"

if __name__ == "__main__":

    screen = init_board() #this draws the board
    main_board = Chessboard()
    main_board.read_FEN(STARTING_BOARD)

    #main game loop
    while (True): 
        #if verify_mate(main_board) (here we exit the game and print some info)
        #move = get_move(main_board)
        #update_board(main_board, move)
        draw_board(main_board, screen) 
