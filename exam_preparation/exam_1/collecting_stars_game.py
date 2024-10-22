n = int(input())
matrix = []
player_position = []
collected_stars = 2
directions = {'up': (-1, 0), 'down': (1, 0), 'left': (0, -1), 'right': (0, 1)}

for row in range(n):
    input_row = input().split()
    matrix.append(input_row)
    for col in range(n):
        if matrix[row][col] == 'P':
            player_position = [row, col]
            matrix[row][col] = '.'


while 0 < collected_stars < 10:
    direction = input()
    next_row, next_col = directions[direction][0] + player_position[0], directions[direction][1] + player_position[1]

    if next_row < 0 or next_row >= n or next_col < 0 or next_col >= n:
        player_position = [0, 0]
        if matrix[0][0] == '*':
            collected_stars += 1
            matrix[0][0] = '.'
        continue

    elif matrix[next_row][next_col] == '*':
        collected_stars += 1
        matrix[next_row][next_col] = '.'
        player_position = [next_row, next_col]
        continue

    elif matrix[next_row][next_col] == '#':
        collected_stars -= 1
        continue

    elif matrix[next_row][next_col] == '.':
        player_position = [next_row, next_col]
        continue

matrix[player_position[0]][player_position[1]] = 'P'

if collected_stars == 10:
    print("You won! You have collected 10 stars.")
else:
    print("Game over! You are out of any stars.")

print(f"Your final position is [{player_position[0]}, {player_position[1]}]")
[print(*row) for row in matrix]





