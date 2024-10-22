def check_matrix_boundaries(x, y, matrix_size):
    if x < 0 or x >= matrix_size or y < 0 or y >= matrix_size:
        return False
    return True


traveler_position = None
health = 100
matrix = []

directions = {'up': (-1, 0), 'down': (1, 0), 'left': (0, -1), 'right': (0, 1)}

n = int(input())

for row in range(n):
    row_data = list(input())
    matrix.append(row_data)
    for col in range(n):
        if matrix[row][col] == 'P':
            traveler_position = [row, col]
            matrix[row][col] = '-'

while True:
    command = input()
    next_row, next_col = traveler_position[0] + directions[command][0], traveler_position[1] + directions[command][1]

    if not check_matrix_boundaries(next_row, next_col, n):
        continue

    if matrix[next_row][next_col] == 'M':
        health -= 40
        if health <= 0:
            health = 0
            traveler_position = [next_row, next_col]
            break
        else:
            matrix[next_row][next_col] = '-'

    elif matrix[next_row][next_col] == 'H':
        health += 15
        matrix[next_row][next_col] = '-'
        if health > 100:
            health = 100

    elif matrix[next_row][next_col] == 'X':
        traveler_position = [next_row, next_col]
        break

    traveler_position = [next_row, next_col]

matrix[traveler_position[0]][traveler_position[1]] = 'P'

if health <= 0:
    print("Player is dead. Maze over!")
else:
    print("Player escaped the maze. Danger passed!")

print(f"Player's health: {health} units")
[print(''.join(row)) for row in matrix]



