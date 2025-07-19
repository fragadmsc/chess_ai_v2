import utils
import board

class Move:
    __slots__ = ("sta", "end")

    def __init__(self, sta: tuple = None, end: tuple = None) -> None:
        self.sta = sta
        self.end = end

def ray_collision_check(chessboard: board.Chessboard, start: tuple, end: tuple) -> bool:
    """checks for collisions in a ray attack (like bishops, rooks, and queens). returns true is there is no collision in start (exclusive, because the piece is there) and end (inclusive)"""
    
def check_move_pawn(chessboard: board.Chessboard, move: Move) -> bool:
    """checks if a pawn is able to do this move in the chessboard, considering that other pieces may prevent his movement"""

def check_move_bishop(chessboard: board.Chessboard, move: Move) -> bool:
    """checks if a bishop is able to do this move in the chessboard, considering that other pieces may prevent his movement"""

def check_move_knight(chessboard: board.Chessboard, move: Move) -> bool:
    """checks if a knight is able to do this move in the chessboard, considering that other pieces may prevent his movement"""

def check_move_rook(chessboard: board.Chessboard, move: Move) -> bool:
    """checks if a rook is able to do this move in the chessboard, considering that other pieces may prevent his movement"""

def check_move_queen(chessboard: board.Chessboard, move: Move) -> bool:
    """checks if a pawn is able to do this move in the chessboard, considering that other pieces may prevent his movement"""

def check_move_king(chessboard: board.Chessboard, move: Move) -> bool:
    """checks if a pawn is able to do this move in the chessboard, considering that other pieces may prevent his movement"""