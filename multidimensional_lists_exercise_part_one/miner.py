def check_position(row, col, size):
    if row in range(size) and col in range(size):
        return True
    return False


matrix_size = int(input())
commands = input().split()
matrix = [[symbol for symbol in input().split()] for _ in range(matrix_size)]
miner_position = None
total_coal = 0
collected_coal = 0

directions = {
    'up': (-1, 0),
    'down': (1, 0),
    'left': (0, -1),
    'right': (0, 1)
}

for row in range(matrix_size):
    for col in range(matrix_size):
        if matrix[row][col] == 's':
            miner_position = [row, col]
        elif matrix[row][col] == 'c':
            total_coal += 1

for command in commands:
    r, c = miner_position[0] + directions[command][0], miner_position[1] + directions[command][1]

    if not check_position(r, c, matrix_size):
        continue

    miner_position = [r, c]

    if matrix[r][c] == 'c':
        collected_coal += 1
        matrix[r][c] = '*'

        if collected_coal == total_coal:
            print(f"You collected all coal! ({r}, {c})")
            break

    elif matrix[r][c] == 'e':
        print(f"Game over! ({r}, {c})")
        break
else:
    print(f"{total_coal - collected_coal} pieces of coal left. ({r}, {c})")