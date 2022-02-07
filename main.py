player_one = None
player_two = None
import math





def check_availability(element, board):

    for i in range(0, len(board)):
        if element in board[i]:
            return True
    return False

over = False

def check_if_won(current, board):
    var = over

    if check_availability(' ', board):
        global loop
        first_row = all([x==current[1] for x in board[0]])
        second_row = all([x == current[1] for x in board[1]])
        third_row = all([x == current[1] for x in board[2]])
        first_column = all(x == current[1] for x in [board[0][0], board[1][0], board[2][0]])
        second_column =all(x == current[1] for x in [board[0][1], board[1][1], board[2][1]])
        third_column = all(x == current[1] for x in [board[0][2], board[1][2], board[2][2]])
        first_diagonal = all(x == current[1] for x in [board[0][0], board[1][1], board[2][2]])
        second_diagonal = all(x == current[1] for x in [board[2][0], board[1][1], board[0][2]])
        if any([first_row, second_row, third_row, first_column, second_column, third_column, first_diagonal, second_diagonal]):
            print(f"{current[0]} won!")
            loop = False
    else:
        var = True
        return var




def setup():
    global player_one, player_two
    player_one_name = input('Player one name: ')
    player_two_name = input("Player two name: ")
    while True:
        player_one_sign = input(f"{player_one_name} would you like to play with 'X' or 'O'?")
        if player_one_sign != 'X' and player_one_sign!= 'O':
            print("Invalid letter! You can only play with 'X' or 'O'")
            continue

        else:
            player_two_sign = 'X' if player_one_sign == 'O' else 'O'
        player_one = [player_one_name, player_one_sign]
        player_two = [player_two_name, player_two_sign]
        print('This is the numeration of the board:')
        print("| 1 | 2 | 3 |")
        print("| 4 | 5 | 6 |")
        print("| 7 | 8 | 9 |")
        print(f"{player_one_name} starts first")
        break


def draw_board(board):
    for row in board:
        print('| ', end="")
        print(' | '.join([str(x) for x in row]), end = "")
        print(' |')




def play(current, board):

    while True:
        choice = int(input(f"{current[0]} choose a free position [1-9]: "))
        if choice < 1 or choice > 9:
            print('Invalid position! Please choose a different one')
            continue

        else:
            row = math.ceil(choice / 3) - 1
            col = choice % 3 - 1
            if board[row][col] != 'X' and board[row][col] != 'O':
                board[row][col] = current[1]
                draw_board(board)
                print(board)
                if check_availability(' ', board):
                    check_if_won(current, board)
                else:
                    over = True
                    new_V = over
                    if new_V:
                        break


            else:
                print('Taken position! Please choose a different one')
                continue
            break





board = [[" ", " ", " "], [" ", " ", " "], [" ", " ", " "]]
setup()
current = player_one
other = player_two
loop = True

#over = True

while loop:
    play(current, board)
    if(check_if_won(current, board) == True):
        print('Nobody wins. End of game')
        break
    current,other = other,current




























