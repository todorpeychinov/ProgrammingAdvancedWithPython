def calc_next_row_and_col(current_position, direction):
    directions = {'up': (-1, 0), 'down': (1, 0), 'left': (0, -1), 'right': (0, 1)}
    return current_position[0] + directions[direction][0], current_position[1] + directions[direction][1]


MATRIX_SIZE = 6
matrix = []

for row in range(6):
    matrix.append(input().split())

user_input = input()
position = (int(user_input[1]), int(user_input[4]))

while True:
    command = input().split(', ')

    if command[0] == "Stop":
        break

    elif command[0] == "Create":
        direction = command[1]
        value = command[2]
        next_row, next_col = calc_next_row_and_col(position, direction)
        if matrix[next_row][next_col] == '.':
            matrix[next_row][next_col] = value
        position = (next_row, next_col)

    elif command[0] == "Update":
        direction = command[1]
        value = command[2]
        next_row, next_col = calc_next_row_and_col(position, direction)
        if matrix[next_row][next_col] != '.':
            matrix[next_row][next_col] = value
        position = (next_row, next_col)

    elif command[0] == "Delete":
        direction = command[1]
        next_row, next_col = calc_next_row_and_col(position, direction)
        if matrix[next_row][next_col] != '.':
            matrix[next_row][next_col] = '.'
        position = (next_row, next_col)

    elif command[0] == "Read":
        direction = command[1]
        next_row, next_col = calc_next_row_and_col(position, direction)
        if matrix[next_row][next_col] != '.':
            print(matrix[next_row][next_col])
        position = (next_row, next_col)

[print(*row) for row in matrix]





