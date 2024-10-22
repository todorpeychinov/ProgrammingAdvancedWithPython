def check_matrix_boundaries(row, col, row_size, col_size):
    if row < 0 or row >= row_size or col < 0 or col >= col_size:
        return False
    return True


directions = {'up': (-1, 0), 'down': (1, 0), 'left': (0, -1), 'right': (0, 1)}
matrix = []

n, m = map(int, input().split(','))
mouse_position = None
cheese_count = 0

for row in range(n):
    matrix.append(list(input()))
    for col in range(m):
        if matrix[row][col] == 'M':
            matrix[row][col] = '*'
            mouse_position = [row, col]
        if matrix[row][col] == 'C':
            cheese_count += 1

while True:
    command = input()

    if command == 'danger':
        if cheese_count > 0:
            print("Mouse will come back later!")
        break

    new_row, new_col = mouse_position[0] + directions[command][0], mouse_position[1] + directions[command][1]

    if not check_matrix_boundaries(new_row, new_col, n, m):
        print("No more cheese for tonight!")
        break

    if matrix[new_row][new_col] == 'C':
        matrix[new_row][new_col] = '*'
        cheese_count -= 1
        mouse_position = [new_row, new_col]

        if cheese_count == 0:
            print("Happy mouse! All the cheese is eaten, good night!")
            break

    elif matrix[new_row][new_col] == 'T':
        mouse_position = [new_row, new_col]
        print("Mouse is trapped!")
        break

    elif matrix[new_row][new_col] == '@':
        continue

    elif matrix[new_row][new_col] == '*':
        mouse_position = [new_row, new_col]

matrix[mouse_position[0]][mouse_position[1]] = 'M'
[print(*row, sep='') for row in matrix]

