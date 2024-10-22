def calc_next_row_and_col(current_position, direction):
    directions = {'up': (-1, 0), 'down': (1, 0), 'left': (0, -1), 'right': (0, 1)}
    return (current_position[0] + directions[direction][0]), (current_position[1] + directions[direction][1])


def is_valid_row_and_col(position, n):
    if 0 <= position[0] < n and 0 <= position[1] < n:
        return True
    return False


def check_upper_left_diagonal(current_position, m_size, board):
    position = current_position
    while True:
        next_row, next_col = calc_next_row_and_col(position, direction='up')
        position = (next_row, next_col)
        next_row, next_col = calc_next_row_and_col(position, direction='left')
        position = (next_row, next_col)
        if is_valid_row_and_col(position, m_size):
            if board[next_row][next_col] == 'Q':
                return False
            elif board[next_row][next_col] == 'K':
                return True
            else:
                continue
        else:
            return False


def check_upper_right_diagonal(current_position, m_size, board):
    position = current_position
    while True:
        next_row, next_col = calc_next_row_and_col(position, direction='up')
        position = (next_row, next_col)
        next_row, next_col = calc_next_row_and_col(position, direction='right')
        position = (next_row, next_col)
        if is_valid_row_and_col(position, m_size):
            if board[next_row][next_col] == 'Q':
                return False
            elif board[next_row][next_col] == 'K':
                return True
            else:
                continue
        else:
            return False


def check_bottom_right_diagonal(current_position, m_size, board):
    position = current_position
    while True:
        next_row, next_col = calc_next_row_and_col(position, direction='down')
        position = (next_row, next_col)
        next_row, next_col = calc_next_row_and_col(position, direction='right')
        position = (next_row, next_col)
        if is_valid_row_and_col(position, m_size):
            if board[next_row][next_col] == 'Q':
                return False
            elif board[next_row][next_col] == 'K':
                return True
            else:
                continue
        else:
            return False


def check_bottom_left_diagonal(current_position, m_size, board):
    position = current_position
    while True:
        next_row, next_col = calc_next_row_and_col(position, direction='down')
        position = (next_row, next_col)
        next_row, next_col = calc_next_row_and_col(position, direction='left')
        position = (next_row, next_col)
        if is_valid_row_and_col(position, m_size):
            if board[next_row][next_col] == 'Q':
                return False
            elif board[next_row][next_col] == 'K':
                return True
            else:
                continue
        else:
            return False



def check_upper_vertical(current_position, m_size, board):
    position = current_position
    while True:
        next_row, next_col = calc_next_row_and_col(position, direction='up')
        position = (next_row, next_col)
        if is_valid_row_and_col(position, m_size):
            if board[next_row][next_col] == 'Q':
                return False
            elif board[next_row][next_col] == 'K':
                return True
            else:
                continue
        else:
            return False


def check_down_vertical(current_position, m_size, board):
    position = current_position
    while True:
        next_row, next_col = calc_next_row_and_col(position, direction='down')
        position = (next_row, next_col)
        if is_valid_row_and_col(position, m_size):
            if board[next_row][next_col] == 'Q':
                return False
            elif board[next_row][next_col] == 'K':
                return True
            else:
                continue
        else:
            return False


def check_left_horizontal(current_position, m_size, board):
    position = current_position
    while True:
        next_row, next_col = calc_next_row_and_col(position, direction='left')
        position = (next_row, next_col)
        if is_valid_row_and_col(position, m_size):
            if board[next_row][next_col] == 'Q':
                return False
            elif board[next_row][next_col] == 'K':
                return True
            else:
                continue
        else:
            return False



def check_right_horizontal(current_position, m_size, board):
    position = current_position
    while True:
        next_row, next_col = calc_next_row_and_col(position, direction='right')
        position = (next_row, next_col)
        if is_valid_row_and_col(position, m_size):
            if board[next_row][next_col] == 'Q':
                return False
            elif board[next_row][next_col] == 'K':
                return True
            else:
                continue
        else:
            return False



def check_positions(current_position, m_size, board):
    if (check_upper_left_diagonal(current_position, m_size, board) or
    check_upper_right_diagonal(current_position, m_size, board) or
    check_bottom_right_diagonal(current_position, m_size, board) or
    check_bottom_left_diagonal(current_position, m_size, board) or
    check_left_horizontal(current_position, m_size, board) or
    check_right_horizontal(current_position, m_size, board) or
    check_down_vertical(current_position, m_size, board) or
    check_upper_vertical(current_position, m_size, board)):
        return True
    return False


BOARD_SIZE = 8
matrix = []
queens_positions = []
king_position = None
attacker_queens = []

for row in range(BOARD_SIZE):
    matrix.append(input().split())
    for col in range(BOARD_SIZE):
        if matrix[row][col] == 'Q':
            queens_positions.append((row, col))
        if matrix[row][col] == 'K':
            king_position = (row, col)

for position in queens_positions:
    if check_positions(position, BOARD_SIZE, matrix):
        attacker_queens.append(list(position))

if attacker_queens:
    print(*attacker_queens, sep='\n')
else:
    print("The king is safe!")




