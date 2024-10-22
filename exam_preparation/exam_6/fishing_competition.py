def check_matrix_boundaries(x, y, matrix_size):
    if x < 0 or x >= matrix_size or y < 0 or y >= matrix_size:
        return False
    return True


directions = {'up': (-1, 0), 'down': (1, 0), 'left': (0, -1), 'right': (0, 1)}
matrix = []
my_position = None
collected_passages = 0
MINIMUM_CATCH = 20

n = int(input())


for row in range(n):
    matrix.append(list(input()))
    for col in range(n):
        if matrix[row][col] == 'S':
            my_position = [row, col]
            matrix[row][col] = '-'

while True:
    command = input()

    if command == 'collect the nets':
        if collected_passages >= MINIMUM_CATCH:
            print("Success! You managed to reach the quota!")
        else:
            print(f"You didn't catch enough fish and didn't reach the quota! You need {MINIMUM_CATCH - collected_passages} tons of fish more.")

        if collected_passages > 0:
            print(f"Amount of fish caught: {collected_passages} tons.")

        matrix[my_position[0]][my_position[1]] = 'S'
        [print(*row, sep='') for row in matrix]
        break

    next_row, next_col = my_position[0] + directions[command][0], my_position[1] + directions[command][1]

    if not check_matrix_boundaries(next_row, next_col, n):
        if next_row >= n:
            next_row = 0
        if next_row < 0:
            next_row = n - 1
        if next_col >= n:
            next_col = 0
        if next_col < 0:
            next_col = n - 1

    my_position = [next_row, next_col]

    if matrix[next_row][next_col].isdigit():
        collected_passages += int(matrix[next_row][next_col])
        matrix[next_row][next_col] = '-'

    elif matrix[next_row][next_col] == 'W':
        collected_passages = 0
        print(f"You fell into a whirlpool! The ship sank and you lost the fish you caught. Last coordinates of the ship: [{my_position[0]},{my_position[1]}]")
        break







