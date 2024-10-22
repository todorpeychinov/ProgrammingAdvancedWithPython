def find_valid_coordinates(r, c, size):
    '''
    123
    4x6
    788
    '''

    coordinates = []

    if r - 1 in range(size) and c - 1 in range(size):
        coordinates.append((r - 1, c - 1))
    if r - 1 in range(size) and c in range(size):
        coordinates.append((r - 1, c))
    if r - 1 in range(size) and c + 1 in range(size):
        coordinates.append((r - 1, c + 1))
    if r in range(size) and c - 1 in range(size):
        coordinates.append((r, c - 1))
    if r in range(size) and c + 1 in range(size):
        coordinates.append((r, c + 1))
    if r + 1 in range(size) and c - 1 in range(size):
        coordinates.append((r + 1, c - 1))
    if r + 1 in range(size) and c in range(size):
        coordinates.append((r + 1, c))
    if r + 1 in range(size) and c + 1 in range(size):
        coordinates.append((r + 1, c + 1))
    return coordinates


matrix_size = int(input())
matrix = [[int(num) for num in input().split()] for _ in range(matrix_size)]
bombs = input().split()

sum = 0
alive_cells = 0


for bomb in bombs:
    row, col = [int(num) for num in bomb.split(',')]

    bomb_size = matrix[row][col]

    if bomb_size > 0:
        coordinates = find_valid_coordinates(row, col, matrix_size)
        for coordinate in coordinates:
            if matrix[coordinate[0]][coordinate[1]] > 0:
                matrix[coordinate[0]][coordinate[1]] -= bomb_size
        matrix[row][col] = 0


for row in range(matrix_size):
    for col in range(matrix_size):
        if matrix[row][col] > 0:
            alive_cells += 1
            sum += matrix[row][col]

print(f"Alive cells: {alive_cells}")
print(f"Sum: {sum}")
[print(*el) for el in matrix]