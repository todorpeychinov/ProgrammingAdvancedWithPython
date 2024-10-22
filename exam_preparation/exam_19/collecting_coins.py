from math import floor


def calc_next_row_and_col(current_position, direction, row_num, col_num, directions):
    return (current_position[0] + directions[direction][0]) % row_num, (current_position[1] + directions[direction][1]) % col_num


directions = {'up': (-1, 0), 'down': (1, 0), 'left': (0, -1), 'right': (0, 1)}

player_position = None
n = int(input())
matrix = []
player_path = []
collected_coins = 0

for row in range(n):
    matrix.append(input().split())
    for col in range(n):
        if matrix[row][col] == 'P':
            player_position = [row, col]
            player_path.append(player_position)
            matrix[row][col] = '-'

while True:
    command = input()

    if command not in directions:
        continue

    next_row, next_col = calc_next_row_and_col(player_position, command, n, n, directions)
    player_position = [next_row, next_col]
    player_path.append(player_position)

    if matrix[next_row][next_col].isdigit():
        collected_coins += int(matrix[next_row][next_col])
        matrix[next_row][next_col] = '-'
        if collected_coins >= 100:
            print(f"You won! You've collected {floor(collected_coins)} coins.")
            break

    elif matrix[next_row][next_col] == 'X':
        collected_coins = floor(collected_coins / 2)
        print(f"Game over! You've collected {collected_coins} coins.")
        break

print("Your path:")
print(*player_path, sep='\n')





