n = int(input())

alice_position = []
collected_bags_of_tea = 0
matrix = []
directions = {'up': (-1, 0), 'down': (1, 0), 'left': (0, -1), 'right': (0, 1)}

for row in range(n):
    row_data = input().split()
    matrix.append(row_data)
    for col in range(n):
        if matrix[row][col] == 'A':
            matrix[row][col] = '*'
            alice_position = [row, col]

while collected_bags_of_tea < 10:
    command = input()

    new_row, new_col = alice_position[0] + directions[command][0], alice_position[1] + directions[command][1]

    if 0 <= new_row < n and 0 <= new_col < n:
        if matrix[new_row][new_col] == 'R':
            matrix[new_row][new_col] = '*'
            break
        elif matrix[new_row][new_col] not in '.*':
            collected_bags_of_tea += int(matrix[new_row][new_col])
        matrix[new_row][new_col] = '*'
        alice_position = [new_row, new_col]
    else:
        break

if collected_bags_of_tea < 10:
    print("Alice didn't make it to the tea party.")
else:
    print("She did it! She went to the party.")
[print(*row) for row in matrix]


