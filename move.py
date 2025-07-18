import utils
import board

class Move:
    __slots__ = ("sta", "end")

    def __init__(self, sta: str = None, end: str = None) -> None:
        self.sta = sta
        self.end = end

def check_valid_move_notation(move: str) -> bool:
    """check if the move is in a valid notation 
    (doesnt check if the numbers are in range 1-8 and the letters in range a-h)"""

    if (move[0].islower() and move[1].isdigit() and
        move[2].islower() and move[1].isdigit()):
        return True
    
    return False

def check_friendly_piece_on_square(move: Move, board : board.Chessboard) -> str:
    """returns the piece if there is a friendly piece (a piece from the player who has the current turn) and returns None is not"""

    starting_square = utils.algebraic_to_pair_notation(move.sta)
    if utils.access_board_with_tuple(board, starting_square)[0] == board.turn:
        return utils.access_board_with_tuple(board, starting_square)[1] #returns the piece
    else:
        return None

def get_move(chessboard: board.Chessboard) -> Move:
    """gets a valid move from the stdin, considering the notation e2e4* (starting square + ending square + the piece that a pawn will promote to (this is present only if the pawn will actually promote)). if the move is 'quit' it will return 'quit'"""

    return_move = Move()
    piece = None

    while (True):
        unchecked_move = input("Digit your move: ").strip()

        if unchecked_move == 'quit':
            return 'quit'
        
        if check_valid_move_notation(unchecked_move):
            return_move.sta = unchecked_move[0:2]
            return_move.end = unchecked_move[2:4]
        else: continue

        if check_friendly_piece_on_square(unchecked_move, board) != None:
            piece = check_friendly_piece_on_square(unchecked_move, board)

        

    


