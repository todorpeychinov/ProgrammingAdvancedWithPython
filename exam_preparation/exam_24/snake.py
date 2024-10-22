def calc_next_row_and_col(current_position, direction):
    directions = {'up': (-1, 0), 'down': (1, 0), 'left': (0, -1), 'right': (0, 1)}
    return (current_position[0] + directions[direction][0]), (current_position[1] + directions[direction][1])


def is_available_position(row, col, m_size):
    if 0 <= row < m_size and 0 <= col < m_size:
        return True
    return False


n = int(input())
snake_position = None
matrix = []
lairs = []

food_eaten = 0

for row in range(n):
    matrix.append(list(input()))
    for col in range(n):
        if matrix[row][col] == 'S':
            snake_position = (row, col)
            matrix[row][col] = '.'
        if matrix[row][col] == 'B':
            lairs.append((row, col))


while True:
    command = input()
    next_row, next_col = calc_next_row_and_col(snake_position, command)

    if is_available_position(next_row, next_col, n):
        snake_position = (next_row, next_col)
        if matrix[next_row][next_col] == '*':
            matrix[next_row][next_col] = '.'
            food_eaten += 1
            if food_eaten == 10:
                matrix[next_row][next_col] = 'S'
                print("You won! You fed the snake.")
                break
        elif matrix[next_row][next_col] == 'B':
            if next_row == lairs[0][0] and next_col == lairs[0][1]:
                snake_position = (lairs[1][0], lairs[1][1])
            else:
                snake_position = (lairs[0][0], lairs[0][1])
            matrix[lairs[0][0]][lairs[0][1]] = '.'
            matrix[lairs[1][0]][lairs[1][1]] = '.'
        elif matrix[next_row][next_col] == '-':
            matrix[next_row][next_col] = '.'
    else:
        print("Game over!")
        break

print(f"Food eaten: {food_eaten}")
[print(*row, sep='') for row in matrix]


