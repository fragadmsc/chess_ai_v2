#from update_board.py import update_board
import utils

BOARD_SIZE = 8
CASTLE_MASK_SIZE = 4

WHITE = 'w'
BLACK = 'b'

KNIGHT = 'N'
QUEEN  = 'Q' 
ROOK   = 'R'
KING   = 'K'
BISHOP = 'B'
PAWN   = 'P'


class chessboard_class:

    __slots__ = ("board", "turn", "castle_rights", "en_passant_square", "move_count", "halfmove_clock", "move list")

    def __init__(self):
        self.board = [['-' for i in range(BOARD_SIZE)] for i in range(BOARD_SIZE)]
        self.turn  = WHITE
        #im using a bitmask for representing castle rights. the order is, respectively white kingside, white queenside, black kingside, black queenside (as in FEN notation)
        self.castle_rights = 0b1111 
        #there is always only one square where en passant can happen. This square is armazenated as a single integer in the range (0-63) or -1 if there isnt a square where en passant can happen. The en passant square is defined to be the square to which the enemy pawn will move if it captures en passant.
        self.en_passant_square = -1
        #move count (always incremented after blacks turn) and halfmove clock (for the 50-move rule)
        self.move_count = 1
        self.halfmove_clock = 0
        #move list
        self.move_list = []



    def export_FEN(self):
        """
        exports the board in a FEN notation, returning the string referent to the board
        """

        fen = ''

        #making the fen string for the board
        for i in range(7, -1, -1):
            cnt = 0
            for j in range(BOARD_SIZE):
                tile = self.board[i][j]
                if (tile == '-'):
                    cnt += 1
                else:
                    if (cnt > 0): fen += str(cnt)
                    if (tile[0] == 'w'): fen += tile[1].upper()
                    else: fen += tile[1].lower()
                    cnt = 0;

            if (cnt > 0): fen += str(cnt)
            fen = fen + '/'

        #adding turn, castle rights, en passant, move count and half move clock
        #turn
        fen = fen + f" {self.turn}"

        #castle
        fen += ' '
        castles = ['K', 'Q', 'k', 'q']
        for i in range(CASTLE_MASK_SIZE):
            if(self.castle_rights & (1<<i)):
                fen = fen + castles[i]
        if (self.castle_rights & ((1<<CASTLE_MASK_SIZE)-1)): #in case that are no castle rights
            fen = fen + '-'

        #en passant
        fen += ' '
        if (self.en_passant_square != -1):
            fen += utils.number_to_algebraic_notation(self.en_passant_square)
        else:
            fen += '-'

        #halfmove rule
        fen += f" {self.halfmove_clock}"

        #move count
        fen += f" {self.move_count}"

        return fen

    
    def read_FEN(self, fen_notation):
        """
        reads a string in a FEN notation and puts it in the self.board
        """
        rows = fen_notation.split(sep = r"[/ ]")

        #reading the basic board
        for fliped_index in range(8):
            row = rows[fliped_index]
            
            row_index = BOARD_SIZE - 1 - fliped_index
            collumn_index = 0
            for ch in row:
                if ch.isdigit():
                    for i in range(int(ch)):
                        self.board[row_index][collumn_index+i] = '-'
                    collumn_index += int(ch)
                else:
                    self.board[row_index][collumn_index] = utils.fen_to_fraga_notation(ch)
                    collumn_index += 1

        #



        



if __name__ == "__main__":

    main_board = chessboard_class()


    #main game loop
    while (True): 
        #update_board(main_board)
        a = 5