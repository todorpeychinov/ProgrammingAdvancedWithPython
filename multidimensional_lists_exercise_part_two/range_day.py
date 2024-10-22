SIZE = 5
matrix = []
my_position = []
targets = 0
shot_targets = []
directions = {'up': (-1, 0), 'down': (1, 0), 'left': (0, -1), 'right': (0, 1)}

for row in range(SIZE):
    row_data = input().split()
    matrix.append(row_data)
    for col in range(SIZE):
        if matrix[row][col] == 'A':
            matrix[row][col] = '.'
            my_position = [row, col]
        if matrix[row][col] == 'x':
            targets += 1

for _ in range(int(input())):
    command = input().split()

    if command[0] == 'shoot':
        direction = command[1]
        r, c = my_position[0], my_position[1]
        while True:
            next_row, next_col = r + directions[direction][0], c + directions[direction][1]
            if 0 <= next_row < SIZE and 0 <= next_col < SIZE:
                if matrix[next_row][next_col] == 'x':
                    shot_targets.append([next_row, next_col])
                    matrix[next_row][next_col] = '.'
                    targets -= 1
                    break
                else:
                    r, c = next_row, next_col
            else:
                break
    elif command[0] == 'move':
        direction = command[1]
        steps = int(command[2])

        next_row, next_col = my_position[0] + directions[direction][0] * steps, my_position[1] + directions[direction][1] * steps
        if 0 <= next_row < SIZE and 0 <= next_col < SIZE and matrix[next_row][next_col] == '.':
            matrix[next_row][next_col] = 'A'
            matrix[my_position[0]][my_position[1]] = '.'
            my_position = [next_row, next_col]

    if targets == 0:
        print(f"Training completed! All {len(shot_targets)} targets hit.")
        break

else:
    print(f"Training not completed! {targets} targets left.")
[print(shot) for shot in shot_targets]