presents = int(input())
n = int(input())
nice_kids = 0
presents_given_to_nice_kids = 0
matrix = []
santa_position = []
directions = {'up': (-1, 0), 'down': (1, 0), 'left': (0, -1), 'right': (0, 1)}

for row in range(n):
    row_data = input().split()
    matrix.append(row_data)
    for col in range(n):
        if matrix[row][col] == 'S':
            matrix[row][col] = '-'
            santa_position = [row, col]
        elif matrix[row][col] == 'V':
            nice_kids += 1

while presents > 0:
    command = input()
    if command == 'Christmas morning':
        break

    next_row, next_col = santa_position[0] + directions[command][0], santa_position[1] + directions[command][1]

    if 0 <= next_row < n and 0 <= next_col < n:
        if matrix[next_row][next_col] == 'X':
            matrix[next_row][next_col] = '-'
            presents -= 1
        elif matrix[next_row][next_col] == 'V':
            matrix[next_row][next_col] = '-'
            presents_given_to_nice_kids += 1
            presents -= 1
        elif matrix[next_row][next_col] == 'C':
            for r, c in directions.values():
                new_row, new_col = next_row + r, next_col + c
                if 0 <= new_row < n and 0 <= new_col < n:
                    if matrix[new_row][new_col] == 'V':
                        presents_given_to_nice_kids += 1
                        presents -= 1
                    elif matrix[new_row][new_col] == 'X':
                        presents -= 1
                    matrix[new_row][new_col] = '-'
                    if presents == 0:
                        break
        matrix[santa_position[0]][santa_position[1]] = '-'
        santa_position = [next_row, next_col]
        matrix[next_row][next_col] = 'S'

if presents == 0 and nice_kids - presents_given_to_nice_kids > 0:
    print("Santa ran out of presents!")
[print(*row) for row in matrix]
if nice_kids - presents_given_to_nice_kids == 0:
    print(f"Good job, Santa! {presents_given_to_nice_kids} happy nice kid/s.")
else:
    print(f"No presents for {nice_kids - presents_given_to_nice_kids} nice kid/s.")
