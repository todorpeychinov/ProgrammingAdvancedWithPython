from math import ceil


class OutOfRangeError(Exception):
    pass


class NotAvailablePosition(Exception):
    pass


class InvalidNumber(Exception):
    pass


def setup_players(name_player_one, name_player_two):
    while True:
        player_one_sign = input(f"{name_player_one} would you like to play with \'X\' or \'O\': ").upper()
        if player_one_sign in ("X", "O"):
            player_two_sign = "X" if player_one_sign == "O" else "O"
            return (name_player_one, player_one_sign), (name_player_two, player_two_sign)
        else:
            print("Player sign must be X or O")


def print_board(current_board):
    for row in current_board:
        print(f'| {" | ".join(str(el) for el in row)} |')


def check_position(current_position, board):
    try:
        player_position = int(current_position)
    except ValueError:
        raise InvalidNumber
    if  player_position > 9 or player_position < 1:
        raise OutOfRangeError

    selected_row_index = ceil(player_position / 3) - 1
    selected_col_index = player_position % 3 - 1

    if board[selected_row_index][selected_col_index] != ' ':
        raise NotAvailablePosition

    return selected_row_index, selected_col_index


def check_winner(board):
    for index in range(3):
        if board[index][0] == board[index][1] == board[index][2] and board[index][0] != ' ':
            return True
        if board[0][index] == board[1][index] == board[2][index] and board[index][0] != ' ':
            return True

    if all([board[i][i] == 'X' for i in range(3)]) or all([board[i][i] == 'O' for i in range(3)]):
        return True

    if all([el == 'X' for el in [board[0][2], board[1][1], board[2][0]]]) or all([el == 'O' for el in [board[0][2], board[1][1], board[2][0]]]):
        return True

    return False


player_one_name = input("Enter player one name: ")
player_two_name = input("Enter player two name: ")
player_one, player_two = setup_players(player_one_name, player_two_name)

num_board = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
print("This is the numeration of the board:")
print_board(num_board)

print(f"{player_one_name} starts first!")
turn = 1
board = [[' ', ' ', ' '] for _ in range(3)]

while True:

    current_player = player_two if turn % 2 == 0 else player_one
    position = input(f"{current_player[0]} choose a free position [1-9]: ")
    try:
        current_row, current_col = check_position(position, board)
    except (OutOfRangeError, InvalidNumber):
        print("Enter a valid position number!")
        continue
    except NotAvailablePosition:
        print("Select a free position!")
        continue

    board[current_row][current_col] = current_player[1]
    turn += 1
    print_board(board)

    if turn > 5:
        have_winner = check_winner(board)
        if have_winner:
            print(f"{current_player[0]} won!")
            break

    if turn == 10:
        print("DRAW! No one wins!")
        break





