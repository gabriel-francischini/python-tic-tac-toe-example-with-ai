from board import print_board
from board import put_symbol
from board import PositionOccupiedError
from board import empty_board
from player_handler import get_user_input
from game_logic import has_winner

is_O = True
is_X = False
symbol = 'O'

player_O_score = 0
player_X_score = 0

board = empty_board()



def update_score(winner, log=False):
    global player_O_score
    global player_X_score

    if winner is None:
        return None
    
    if winner == 'O':
        player_O_score += 1
    elif winner == 'X':
        player_X_score += 1

    if log:
        if winner != '-':
            print("Player " + winner + " wins!")
            print("Current score is: X = "
                  + str(player_X_score)
                  + ", O = " + str(player_O_score) + "\n")
        else:
            print("The game draws!")

    return winner

def play_game(play_func_O=get_user_input,
              play_func_X=get_user_input,
              N=1,
              should_print_board=False):    
    global is_O
    global is_X
    global symbol

    global player_O_score
    global player_X_score

    global board
    #print(N)
    is_O = True
    is_X = False
    symbol = 'O'

    player_O_score = 0
    player_X_score = 0

    board = empty_board()

    game_counter = 0
    while True:
        try:
            if is_O:
                board = put_symbol(board, symbol, play_func_O(board))
                symbol = 'X'
            else:
                board = put_symbol(board, symbol, play_func_X(board))
                symbol = 'O'

            if should_print_board:
                print_board(board)

            is_O = not is_O
            is_X = not is_X

            # If someone wins, empty the board and show the score
            if update_score(has_winner(board), log=should_print_board) is not None:
                board = empty_board()
                is_O = True
                is_X = False
                symbol = 'O'

                game_counter += 1
                if game_counter >= N:
                    return (player_O_score, player_X_score)


        except PositionOccupiedError:
            print("That position is already occupied.")
        except (ValueError, IndexError):
            print("You don't entered a valid position")


