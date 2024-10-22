def show_result(status='won'):
    [print(*row, sep='') for row in matrix]
    print(f'{status}: {player_row} {player_col}')

    raise SystemExit


def check_position(row, col, player=True):
    global wins
    if 0 <= row < rows and 0 <= col < cols:
        return True
    if player:
        wins = True


def check_player(row, col):
    if matrix[row][col] == 'B':
        show_result('dead')


def find_bunnies():
    positions = []

    for row in range(rows):
        for col in range(cols):
            if matrix[row][col] == 'B':
                positions.append([row, col])
    return positions


def move_bunnies(bunnies_pos):
    for row, col in bunnies_pos:
        for bunnie_move in directions.values():
            new_row, new_col = row + bunnie_move[0], col + bunnie_move[1]

            if check_position(new_row, new_col, False):
                matrix[new_row][new_col] = 'B'



rows, cols = [int(num) for num in input().split()]
matrix = [list(input()) for _ in range(rows)]

commands = input()

wins = False

directions = {
    'U': (-1, 0),
    'D': (1, 0),
    'L': (0, -1),
    'R': (0, 1)
}

for row in range(rows):
    for col in range(cols):
        if matrix[row][col] == 'P':
            player_row = row
            player_col = col
            matrix[row][col] = '.'
            break

for command in commands:
    r, c = player_row + directions[command][0], player_col + directions[command][1]

    if check_position(r, c, True):
        player_row = r
        player_col = c

    move_bunnies(find_bunnies())

    if wins:
        show_result('won')

    check_player(player_row, player_col)



