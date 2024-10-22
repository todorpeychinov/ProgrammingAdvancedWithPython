def check_matrix_boundaries(row, col, row_size, col_size):
    if row < 0 or row >= row_size or col < 0 or col >= col_size:
        return False
    return True


directions = {'up': (-1, 0), 'down': (1, 0), 'left': (0, -1), 'right': (0, 1)}
matrix = []
my_position = None
MAX_PLAYERS = 3

n, m = map(int, input().split())
moves = 0
touched_players = 0


for row in range(n):
    matrix.append(input().split())
    for col in range(m):
        if matrix[row][col] == 'B':
            my_position = (row, col)
            matrix[row][col] = '-'

while True:
    command = input()

    if command == 'Finish':
        break

    next_row, next_col = my_position[0] + directions[command][0], my_position[1] + directions[command][1]

    if not check_matrix_boundaries(next_row, next_col, m, n) or matrix[next_row][next_col] == 'O':
        continue

    if matrix[next_row][next_col] == 'P':
        touched_players += 1
        matrix[next_row][next_col] = '-'

    moves += 1
    my_position = (next_row, next_col)

    if touched_players == MAX_PLAYERS:
        break

print("Game over!")
print(f"Touched opponents: {touched_players} Moves made: {moves}")