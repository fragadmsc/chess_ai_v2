BOARD_SIZE = 8

def number_to_algebraic_notation(number):
    row = number // BOARD_SIZE
    collumn = number % BOARD_SIZE
    
    algebraic_notation = chr(collumn + ord('a')) + str(row+1) 
    return algebraic_notation

def reverse_turn(turn):
    if turn == 'w': return 'b'
    return 'w'

def fen_to_fraga_notation(ch):
    """this takes a piece in fen notation and converts it to my notation"""

    ret = ''
    if ch.isupper():
        ret += 'w'
    else:
        ret += 'b'

    ret += ch.upper()
    return ret