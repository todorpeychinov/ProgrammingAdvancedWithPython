def check_matrix_boundaries(row, col, row_size, col_size):
    if row < 0 or row >= row_size or col < 0 or col >= col_size:
        return False
    return True


directions = {'up': (-1, 0), 'down': (1, 0), 'left': (0, -1), 'right': (0, 1)}
matrix = []
car_position = [0, 0]
tunnels = []
kilometers = 0

n = int(input())
car_number = input()

for row in range(n):
    matrix.append(input().split())
    for col in range(n):
        if matrix[row][col] == 'T':
            tunnels.append((row, col))

while True:
    command = input()

    if command == "End":
        print(f"Racing car {car_number} DNF.")
        break

    next_row, next_col = car_position[0] + directions[command][0], car_position[1] + directions[command][1]

    if matrix[next_row][next_col] == '.':
        kilometers += 10
        car_position = [next_row, next_col]

    elif matrix[next_row][next_col] == 'T':
        matrix[next_row][next_col] = '.'
        if next_row == tunnels[0][0] and next_col == tunnels[0][1]:
            car_position = [tunnels[1][0], tunnels[1][1]]
            matrix[tunnels[1][0]][tunnels[1][1]] = '.'
        else:
            car_position = [tunnels[0][0], tunnels[0][1]]
            matrix[tunnels[0][0]][tunnels[0][1]] = '.'
        kilometers += 30

    elif matrix[next_row][next_col] == 'F':
        print(f"Racing car {car_number} finished the stage!")
        kilometers += 10
        car_position = [next_row, next_col]
        break


print(f"Distance covered {kilometers} km.")
matrix[car_position[0]][car_position[1]] = 'C'
[print(*row, sep='') for row in matrix]




