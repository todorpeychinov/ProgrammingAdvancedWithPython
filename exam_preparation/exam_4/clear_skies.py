def check_matrix_boundaries(x, y, matrix_size):
    if x < 0 or x >= matrix_size or y < 0 or y >= matrix_size:
        return False
    return True


INITIAL_ARMOR_VALUE = 300

matrix = []
fighter_position = None
armor_value = INITIAL_ARMOR_VALUE
directions = {'up': (-1, 0), 'down': (1, 0), 'left': (0, -1), 'right': (0, 1)}
enemy_plane_count = 0

n = int(input())

for row in range(n):
    row_data = list(input())
    matrix.append(row_data)
    for col in range(n):
        if matrix[row][col] == 'J':
            fighter_position = [row, col]
            matrix[row][col] = '-'
        if matrix[row][col] == 'E':
            enemy_plane_count += 1


while True:
    direction = input()
    next_row, next_col = fighter_position[0] + directions[direction][0], fighter_position[1] + directions[direction][1]

    if check_matrix_boundaries(next_row, next_col, n):
        fighter_position = [next_row, next_col]

        if matrix[next_row][next_col] == '-':
            continue

        elif matrix[next_row][next_col] == 'E':
            matrix[next_row][next_col] = '-'
            enemy_plane_count -= 1
            if enemy_plane_count == 0:
                print("Mission accomplished, you neutralized the aerial threat!")
                break
            else:
                armor_value -= 100
                if armor_value <= 0:
                    print(f"Mission failed, your jetfighter was shot down! Last coordinates [{fighter_position[0]}, {fighter_position[1]}]!")
                    break

        elif matrix[next_row][next_col] == 'R':
            matrix[next_row][next_col] = '-'
            armor_value = 300

matrix[fighter_position[0]][fighter_position[1]] = 'J'
[print(*row, sep='') for row in matrix]



