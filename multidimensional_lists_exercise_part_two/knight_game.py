n = int(input())

removed_knights = 0
knights_positions = []
matrix = []

for row in range(n):
    row_data = list(input())
    matrix.append(row_data)
    for col in range(n):
        if matrix[row][col] == 'K':
            knights_positions.append([row, col])

possible_moves = ((-2, 1), (-1, 2), (1, 2), (2, 1), (2, -1), (1, -2), (-1, -2), (-2, -1))

while True:
    max_attacked = 0
    max_knight = [0, 0]

    for knight_row, knight_col in knights_positions:
        attacked = 0
        for move in possible_moves:
            new_row, new_col = knight_row + move[0], knight_col + move[1]
            if 0 <= new_row < n and 0 <= new_col < n and matrix[new_row][new_col] == 'K':
                attacked += 1
        if attacked > max_attacked:
            max_attacked = attacked
            max_knight = [knight_row, knight_col]

    if max_attacked == 0:
        break

    matrix[max_knight[0]][max_knight[1]] = '0'
    knights_positions.remove([max_knight[0], max_knight[1]])
    removed_knights += 1

print(removed_knights)



