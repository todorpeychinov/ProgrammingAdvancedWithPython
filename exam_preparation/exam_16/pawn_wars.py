def move_white(row, col):
    return row - 1, col


def move_black(row, col):
    return row + 1, col


def move_player(player, row, col):
    if player == 'White':
        return move_white(row, col)
    else:
        return move_black(row, col)


def check_row_and_col(row, col, size):
    if 0 <= row < size and 0 <= col < size:
        return True
    return False


def check_last_rank(row, player):
    if player == 'White':
        if row == 0:
            return True
    if player == 'Black':
        if row == 7:
            return True
    return False


def check_diagonal(player_1_position, player_2_position, current_player):
    if current_player == 'White':
        if player_1_position[0] - 1 == player_2_position[0] and player_1_position[1] - 1 == player_2_position[1]:
            square = board[(player_1_position[0] - 1)][(player_1_position[1] - 1)]
            print(f"Game over! {current_player} win, capture on {square}.")
            return True
        if player_1_position[0] - 1 == player_2_position[0] and player_1_position[1] + 1 == player_2_position[1]:
            square = board[(player_1_position[0] - 1)][(player_1_position[1] + 1)]
            print(f"Game over! {current_player} win, capture on {square}.")
            return True
    if current_player == 'Black':
        if player_2_position[0] + 1 == player_1_position[0] and player_2_position[1] - 1 == player_1_position[1]:
            square = board[(player_2_position[0] + 1)][(player_2_position[1] - 1)]
            print(f"Game over! {current_player} win, capture on {square}.")
            return True
        if player_2_position[0] + 1 == player_1_position[0] and player_2_position[1] + 1 == player_1_position[1]:
            square = board[(player_2_position[0] + 1)][(player_2_position[1] + 1)]
            print(f"Game over! {current_player} win, capture on {square}.")
            return True
    return False


board = [
    ['a8', 'b8', 'c8', 'd8', 'e8', 'f8', 'g8', 'h8'],
    ['a7', 'b7', 'c7', 'd7', 'e7', 'f7', 'g7', 'h7'],
    ['a6', 'b6', 'c6', 'd6', 'e6', 'f6', 'g6', 'h6'],
    ['a5', 'b5', 'c5', 'd5', 'e5', 'f5', 'g5', 'h5'],
    ['a4', 'b4', 'c4', 'd4', 'e4', 'f4', 'g4', 'h4'],
    ['a3', 'b3', 'c3', 'd3', 'e3', 'f3', 'g3', 'h3'],
    ['a2', 'b2', 'c2', 'd2', 'e2', 'f2', 'g2', 'h2'],
    ['a1', 'b1', 'c1', 'd1', 'e1', 'f1', 'g1', 'h1']

]

cols = {
    0: 'a',
    1: 'b',
    2: 'c',
    3: 'd',
    4: 'e',
    5: 'f',
    6: 'g',
    7: 'h'
}

rows = {
    0: '8',
    1: '7',
    2: '6',
    3: '5',
    4: '4',
    5: '3',
    6: '2',
    7: '1'
}

MATRIX_SIZE = 8
player_1 = "White"
player_2 = "Black"
player_1_position = None
player_2_position = None
matrix = []
turn = 1

for row in range(MATRIX_SIZE):
    matrix.append(input().split())
    for col in range(MATRIX_SIZE):
        if matrix[row][col] == 'w':
            player_1_position = (row, col)
        if matrix[row][col] == 'b':
            player_2_position = (row, col)


while True:

    current_player = player_1 if turn % 2 != 0 else player_2
    other_player = player_2 if turn % 2 != 0 else player_1
    turn += 1

    if current_player == 'White':
        curr_row, curr_col = player_1_position[0], player_1_position[1]
    else:
        curr_row, curr_col = player_2_position[0], player_2_position[1]

    if check_last_rank(curr_row, current_player):
        square = cols[curr_col] + rows[curr_row]
        print(f"Game over! {current_player} pawn is promoted to a queen at {square}.")
        break

    if check_diagonal(player_1_position, player_2_position, current_player):
        break

    if current_player == player_1:
        next_row, next_col = move_player(current_player, player_1_position[0], player_1_position[1])
        player_1_position = (next_row, next_col)
    else:
        next_row, next_col = move_player(current_player, player_2_position[0], player_2_position[1])
        player_2_position = (next_row, next_col)




