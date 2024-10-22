n = int(input())
bee_energy = 15
matrix = []
bee_position = []
nectar = 0
directions = {'up': (-1, 0), 'down': (1, 0), 'left': (0, -1), 'right': (0, 1)}
is_reloaded = False

for row in range(n):
    matrix.append(list(input()))
    for col in range(n):
        if matrix[row][col] == 'B':
            bee_position = [row, col]
            matrix[row][col] = '-'

while True:
    command = input()
    next_row, next_col = directions[command][0] + bee_position[0], directions[command][1] + bee_position[1]
    bee_energy -= 1

    if next_row < 0:
        next_row = n - 1
    if next_col < 0:
        next_col = n - 1
    if next_row == n:
        next_row = 0
    if next_col == n:
        next_col = 0

    if matrix[next_row][next_col].isdigit():
        nectar += int(matrix[next_row][next_col])
        matrix[next_row][next_col] = '-'

    if matrix[next_row][next_col] == 'H':
        bee_position = [next_row, next_col]
        matrix[next_row][next_col] = '-'
        if nectar >= 30:
            print(f"Great job, Beesy! The hive is full. Energy left: {bee_energy}")
        else:
            print("Beesy did not manage to collect enough nectar.")
        break

    bee_position = [next_row, next_col]

    if bee_energy == 0:
        if nectar >= 30 and not is_reloaded:
            energy_to_increase = nectar - 30
            bee_energy += energy_to_increase
            nectar = 30
            is_reloaded = True
        else:
            print("This is the end! Beesy ran out of energy.")
            break


matrix[bee_position[0]][bee_position[1]] = 'B'
[print(*row, sep='') for row in matrix]






