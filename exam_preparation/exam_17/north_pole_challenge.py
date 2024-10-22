def calc_next_row_and_col(current_position, direction, row_num, col_num):
    directions = {'up': (-1, 0), 'down': (1, 0), 'left': (0, -1), 'right': (0, 1)}
    return (current_position[0] + directions[direction][0]) % row_num, (current_position[1] + directions[direction][1]) % col_num


rows, cols = map(int, input().split(', '))

matrix = []
my_position = None
is_something_left = True

decorations = 0
gifts = 0
cookies = 0

decorations_left = 0
gifts_left = 0
cookies_left = 0

for row in range(rows):
    matrix.append(input().split())
    for col in range(cols):
        if matrix[row][col] == 'Y':
            my_position = (row, col)
        elif matrix[row][col] == 'D':
            decorations_left += 1
        elif matrix[row][col] == 'G':
            gifts_left += 1
        elif matrix[row][col] == 'C':
            cookies_left += 1


while is_something_left:
    command = input().split('-')

    if command[0] == 'End':
        break

    direction = command[0]
    steps = int(command[1])

    for _ in range(steps):
        next_row, next_col = calc_next_row_and_col(my_position, direction, rows, cols)
        if matrix[next_row][next_col] == 'D':
            decorations += 1
            decorations_left -= 1
        elif matrix[next_row][next_col] == 'G':
            gifts += 1
            gifts_left -= 1
        elif matrix[next_row][next_col] == 'C':
            cookies += 1
            cookies_left -= 1
        matrix[my_position[0]][my_position[1]] = 'x'
        matrix[next_row][next_col] = 'Y'
        my_position = (next_row, next_col)

        if cookies_left == 0 and decorations_left == 0 and gifts_left == 0:
            is_something_left = False
            break


if not is_something_left:
    print("Merry Christmas!")
print("You've collected:")
print(f"- {decorations} Christmas decorations\n"
      f"- {gifts} Gifts\n"
      f"- {cookies} Cookies")
[print(*row) for row in matrix]

