import utils
import board
import piece_move



def check_valid_move_notation(move: str) -> bool:
    """check if the move is in a valid notation 
    (doesnt check if the numbers are in range 1-8 and the letters in range a-h)"""

    if (move[0].islower() and move[1].isdigit() and
        move[2].islower() and move[1].isdigit()):
        return True
    
    return False

def check_friendly_piece_on_square(move: piece_move.Move, board : board.Chessboard) -> str:
    """returns the piece if there is a friendly piece (a piece from the player who has the current turn) and returns None is not"""

    if utils.access_board_with_tuple(board, move.sta)[0] == board.turn:
        return utils.access_board_with_tuple(board, move.sta)[1] #returns the piece
    else:
        return None

def check_move_possible_for_piece(piece: str, move: piece_move.Move, chessboard: board.Chessboard) -> bool:
    """checks if the piece can make this move (ignoring checks). this function check if the piece can make the move (e.g a bishop cannot go up or down) and if there isnt a friendly piece in the ending square or a piece blocking the path"""
    
    if piece == board.PAWN:
        return piece_move.check_move_pawn(chessboard, move)
    if piece == board.BISHOP:
        return piece_move.check_move_bishop(chessboard, move)
    if piece == board.KNIGHT:
        return piece_move.check_move_knight(chessboard, move)
    if piece == board.ROOK:
        return piece_move.check_move_rook(chessboard, move)
    if piece == board.QUEEN:
        return piece_move.check_move_queen(chessboard, move)
    if piece == board.KING:
        return piece_move.check_move_king(chessboard, move)


def check_king_check_after_move(piece: str, move: piece_move.Move, chessboard: board.Chessboard) -> bool:
    """checks if the king of the player in turn will be left in check after the move (this means that the piece is pinned or that the king is in check and must move)"""




def get_move(chessboard: board.Chessboard) -> piece_move.Move:
    """gets a valid move from the stdin, considering the notation e2e4* (starting square + ending square + the piece that a pawn will promote to (this is present only if the pawn will actually promote)). if the move is 'quit' it will return 'quit'"""

    return_move = piece_move.Move()
    piece = None

    while (True):
        unchecked_move = input("Digit your move: ").strip()

        if unchecked_move == 'quit':
            return 'quit'
        
        if check_valid_move_notation(unchecked_move):
            return_move.sta = utils.algebraic_to_pair_notation(unchecked_move[0:2])
            return_move.end = utils.algebraic_to_pair_notation(unchecked_move[2:4])
        else: 
            print("invalid move\n")
            continue

        if check_friendly_piece_on_square(return_move, chessboard) != None:
            piece = check_friendly_piece_on_square(return_move, chessboard)
        
        if not check_move_possible_for_piece(piece, return_move, chessboard):
            print("invalid move\n")
            continue

        if not check_king_check_after_move(piece, return_move, chessboard):
            print("invalid move\n")
            continue
        

    


