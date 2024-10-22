def calc_next_row_and_col(current_position, direction, MATRIX_SIZE):
    directions = {'up': (-1, 0), 'down': (1, 0), 'left': (0, -1), 'right': (0, 1)}
    return (current_position[0] + directions[direction][0]) % MATRIX_SIZE, (current_position[1] + directions[direction][1]) % MATRIX_SIZE


deposits = {
    "Water deposit": 0,
    "Metal deposit": 0,
    "Concrete deposit": 0
}

MATRIX_SIZE = 6
matrix = []

rover_position = None

for row in range(MATRIX_SIZE):
    matrix.append(input().split())
    for col in range(MATRIX_SIZE):
        if matrix[row][col] == 'E':
            matrix[row][col] = '-'
            rover_position = (row, col)

commands = input().split(', ')

for command in commands:
    new_row, new_col = calc_next_row_and_col(rover_position, command, MATRIX_SIZE)
    rover_position = (new_row, new_col)

    if matrix[new_row][new_col] == 'W':
        deposits['Water deposit'] += 1
        print(f'Water deposit found at ({new_row}, {new_col})')

    elif matrix[new_row][new_col] == 'M':
        deposits['Metal deposit'] += 1
        print(f'Metal deposit found at ({new_row}, {new_col})')

    elif matrix[new_row][new_col] == 'C':
        deposits['Concrete deposit'] += 1
        print(f'Concrete deposit found at ({new_row}, {new_col})')

    elif matrix[new_row][new_col] == 'R':
        print(f"Rover got broken at ({new_row}, {new_col})")
        break

if all([value > 0 for value in deposits.values()]):
    print("Area suitable to start the colony.")
else:
    print("Area not suitable to start the colony.")





