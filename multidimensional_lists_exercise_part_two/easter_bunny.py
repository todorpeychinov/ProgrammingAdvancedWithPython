n = int(input())

matrix = []
bunny_position = []
max_eggs = float('-inf')
eggs_positions = None
max_direction = None

directions = {'up': (-1, 0), 'down': (1, 0), 'left': (0, -1), 'right': (0, 1)}

for row in range(n):
    matrix.append(input().split())
    for col in range(n):
        if matrix[row][col] == 'B':
            bunny_position = [row, col]

for direction, position in directions.items():
    r, c = int(bunny_position[0]), int(bunny_position[1])
    current_eggs = 0
    current_eggs_positions = []
    while True:
        new_row, new_col = r + position[0], c + position[1]
        if new_row < 0 or new_row >= n or new_col < 0 or new_col >= n or matrix[new_row][new_col] == 'X':
            break
        else:
            current_eggs += int(matrix[new_row][new_col])
            current_eggs_positions.append([new_row, new_col])
            r, c = new_row, new_col
    if current_eggs > max_eggs and current_eggs_positions:
        max_eggs = current_eggs
        eggs_positions = current_eggs_positions
        max_direction = direction

print(max_direction)
[print(row) for row in eggs_positions]
print(max_eggs)


