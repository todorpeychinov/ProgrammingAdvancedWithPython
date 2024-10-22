def check_matrix_boundaries(x, y, matrix_size):
    if x < 0 or x >= matrix_size or y < 0 or y >= matrix_size:
        return False
    return True


directions = {'up': (-1, 0), 'down': (1, 0), 'left': (0, -1), 'right': (0, 1)}
matrix = []
my_position = None

n, m = [int(el) for el in input().split()]
starting_position = None

for row in range(n):
    row_data = list(input())
    matrix.append(row_data)
    for col in range(m):
        if matrix[row][col] == 'B':
            my_position = [row, col]
            starting_position = [row, col]


while True:
    command = input()

    next_row, next_col = my_position[0] + directions[command][0], my_position[1] + directions[command][1]

    if check_matrix_boundaries(next_row, next_col, m):



        if matrix[next_row][next_col] == 'P':
            print("Pizza is collected. 10 minutes for delivery.")
            matrix[next_row][next_col] = 'R'
            my_position = [next_row, next_col]

        elif matrix[next_row][next_col] == '*':
            continue

        elif matrix[next_row][next_col] == 'A':
            matrix[next_row][next_col] = 'P'
            matrix[my_position[0]][my_position[1]] = '.'
            my_position = [next_row, next_col]
            print("Pizza is delivered on time! Next order...")
            break

        elif matrix[next_row][next_col] == '-':
            my_position = [next_row, next_col]
            matrix[next_row][next_col] = '.'

        elif matrix[next_row][next_col] == '.':
            my_position = [next_row, next_col]

        elif matrix[next_row][next_col] == 'R':
            my_position = [next_row, next_col]

        #my_position = [next_row, next_col]

    else:
        matrix[starting_position[0]][starting_position[1]] = ' '
        print("The delivery is late. Order is canceled.")


[print(*row, sep='') for row in matrix]