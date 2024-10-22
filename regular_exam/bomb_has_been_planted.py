def calc_next_row_and_col(current_position, direction):
    directions = {'up': (-1, 0), 'down': (1, 0), 'left': (0, -1), 'right': (0, 1)}
    return (current_position[0] + directions[direction][0]), (current_position[1] + directions[direction][1])


def is_available_position(row, col, rows, cols):
    if 0 <= row < rows and 0 <= col < cols:
        return True
    return False


n, m = map(int, input().split(', '))
matrix = []
counter_terrorist_position = None
initial_position = None
seconds_remaining = 16
is_bomb_found = False

for row in range(n):
    matrix.append(list(input()))
    for col in range(m):
        if matrix[row][col] == 'C':
            counter_terrorist_position = (row, col)
            initial_position = (row, col)

while True:

    if seconds_remaining == 0:
        print("Terrorists win!")
        print("Bomb was not defused successfully!")
        print(f"Time needed: 0 second/s.")
        break

    command = input()

    if is_bomb_found:
        if command == 'defuse':
            if seconds_remaining >= 4:
                seconds_remaining -= 4
                matrix[counter_terrorist_position[0]][counter_terrorist_position[1]] = 'D'
                print("Counter-terrorist wins!")
                print(f"Bomb has been defused: {seconds_remaining} second/s remaining.")
                break
            else:
                #matrix[initial_position[0]][initial_position[1]] = '*'
                matrix[counter_terrorist_position[0]][counter_terrorist_position[1]] = 'X'
                print("Terrorists win!")
                print("Bomb was not defused successfully!")
                print(f"Time needed: {4 - seconds_remaining} second/s.")
                break
        else:
            is_bomb_found = False

    seconds_remaining -= 1

    if command == 'defuse':
        seconds_remaining -= 1
        continue

    next_row, next_col = calc_next_row_and_col(counter_terrorist_position, command)

    if not is_available_position(next_row, next_col, n, m):
        continue

    elif matrix[next_row][next_col] == '*':
        counter_terrorist_position = (next_row, next_col)
        continue

    elif matrix[next_row][next_col] == 'B':
        counter_terrorist_position = (next_row, next_col)
        is_bomb_found = True
        continue

    elif matrix[next_row][next_col] == 'T':
        matrix[next_row][next_col] = '*'
        #matrix[initial_position[0]][initial_position[1]] = '*'
        print("Terrorists win!")
        break

    elif matrix[next_row][next_col] == 'C':
        counter_terrorist_position = (next_row, next_col)


[print(*row, sep='') for row in matrix]

