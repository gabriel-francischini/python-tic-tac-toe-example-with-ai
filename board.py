class PositionOccupiedError(IndexError):
    pass


def print_board(tabuleiro):
    "This function prints a board."
    for index, linha in enumerate(tabuleiro):
        print('|'.join(linha), end='')
        print('\n-+-+-')

    print("="*80)

def put_symbol(tabuleiro, symbol, posicao):
    copia = list(tabuleiro)
    x, y = posicao

    if tabuleiro[x][y] != ' ':
        raise PositionOccupiedError
    
    copia[x][y] = symbol
    return copia

def empty_board(board=[]):
    return [
        [" ", " ", " "],
        [" ", " ", " "],
        [" ", " ", " "],
    ]
