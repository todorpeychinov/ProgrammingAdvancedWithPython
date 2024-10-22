def calc_next_row_and_col(current_position, direction):
    directions = {'up': (-1, 0), 'down': (1, 0), 'left': (0, -1), 'right': (0, 1)}
    return (current_position[0] + directions[direction][0]), (current_position[1] + directions[direction][1])


def is_available_position(row, col, m_size):
    if 0 <= row < m_size and 0 <= col < m_size:
        return True
    return False


initial_string = input()
n = int(input())

matrix = []
player_position = None

for row in range(n):
    matrix.append(list(input()))
    for col in range(n):
        if matrix[row][col] == 'P':
            player_position = (row, col)
            matrix[row][col] = '-'

number_of_commands = int(input())

for _ in range(number_of_commands):
    command = input()

    next_row, next_col = calc_next_row_and_col(player_position, command)

    if is_available_position(next_row, next_col, n):
        player_position = (next_row, next_col)
        if matrix[next_row][next_col].isalpha():
            initial_string += matrix[next_row][next_col]
            matrix[next_row][next_col] = '-'
    else:
        if len(initial_string) > 0:
            initial_string = initial_string[:-1]

matrix[player_position[0]][player_position[1]] = 'P'
print(initial_string)
[print(*row, sep='') for row in matrix]


