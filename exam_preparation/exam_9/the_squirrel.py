def check_matrix_boundaries(row, col, row_size, col_size):
    if row < 0 or row >= row_size or col < 0 or col >= col_size:
        return False
    return True


directions = {'up': (-1, 0), 'down': (1, 0), 'left': (0, -1), 'right': (0, 1)}
matrix = []

hazelnuts = 0
GOAL = 3
squirrel_position = None

n = int(input())
commands = input().split(', ')

for row in range(n):
    matrix.append(list(input()))
    for col in range(n):
        if matrix[row][col] == 's':
            squirrel_position = (row, col)
            matrix[row][col] = '*'

for command in commands:
    next_row, next_col = squirrel_position[0] + directions[command][0], squirrel_position[1] + directions[command][1]

    if not check_matrix_boundaries(next_row, next_col, n, n):
        print("The squirrel is out of the field.")
        break

    if matrix[next_row][next_col] == 'h':
        matrix[next_row][next_col] = '*'
        squirrel_position = (next_row, next_col)
        hazelnuts += 1
        if hazelnuts == GOAL:
            print("Good job! You have collected all hazelnuts!")
            break

    elif matrix[next_row][next_col] == '*':
        squirrel_position = (next_row, next_col)
        continue

    elif matrix[next_row][next_col] == 't':
        squirrel_position = (next_row, next_col)
        print("Unfortunately, the squirrel stepped on a trap...")
        break
else:
    print('There are more hazelnuts to collect.')

print(f"Hazelnuts collected: {hazelnuts}")