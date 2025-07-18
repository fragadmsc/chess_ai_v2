BOARD_SIZE = 8

def number_to_algebraic_notation(number: int) -> str:
    row = number // BOARD_SIZE
    collumn = number % BOARD_SIZE
    
    algebraic_notation = chr(collumn + ord('a')) + str(row+1) 
    return algebraic_notation

def algebraic_to_number_notation(algebraic: str) -> int:
    ch = algebraic[0]
    n = int(algebraic[1])

    return ord(ch) - ord('a') + 8*(n-1)

def access_board_with_tuple(board, pair: tuple) -> str:
    return board[pair[0]][pair[1]]

def number_to_pair_notation(number: int) -> tuple:
    return (number//BOARD_SIZE, number%BOARD_SIZE)

def algebraic_to_pair_notation(algebraic: str) -> tuple:
    return number_to_pair_notation(algebraic_to_number_notation(algebraic))

def reverse_turn(turn: str) -> str:
    if turn == 'w': return 'b'
    return 'w'

def fen_to_fraga_notation(ch: str) -> str:
    """this takes a piece in fen notation and converts it to my notation"""

    ret = ''
    if ch.isupper():
        ret += 'w'
    else:
        ret += 'b'

    ret += ch.upper()
    return ret