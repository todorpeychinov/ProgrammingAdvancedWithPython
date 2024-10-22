directions = {'up': (-1, 0), 'down': (1, 0), 'left': (0, -1), 'right': (0, 1)}
matrix = []
submarine_position = None

n = int(input())
MAX_ATTACKS_NUM = 2
attacks = 0
MAX_BATTLE_CRUISERS = 3
battle_cruisers = 0

for row in range(n):
    matrix.append(list(input()))
    for col in range(n):
        if matrix[row][col] == 'S':
            matrix[row][col] = '-'
            submarine_position = (row, col)

while True:
    command = input()

    next_row, next_col = submarine_position[0] + directions[command][0], submarine_position[1] + directions[command][1]

    if matrix[next_row][next_col] == '-':
        submarine_position = (next_row, next_col)
        continue
    elif matrix[next_row][next_col] == '*':
        attacks += 1
        matrix[next_row][next_col] = '-'
        submarine_position = (next_row, next_col)
        if attacks > MAX_ATTACKS_NUM:
            print(f"Mission failed, U-9 disappeared! Last known coordinates [{submarine_position[0]}, {submarine_position[1]}]!")
            break
    elif matrix[next_row][next_col] == 'C':
        submarine_position = (next_row, next_col)
        matrix[next_row][next_col] = '-'
        battle_cruisers += 1
        if battle_cruisers == MAX_BATTLE_CRUISERS:
            print("Mission accomplished, U-9 has destroyed all battle cruisers of the enemy!")
            break

matrix[submarine_position[0]][submarine_position[1]] = 'S'
[print(*row, sep='') for row in matrix]





