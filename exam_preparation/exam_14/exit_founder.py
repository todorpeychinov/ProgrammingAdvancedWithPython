player_1, player_2 = input().split(', ')

MATRIX_SIZE = 6
matrix = []
turn = 1
skip_turn_player_one = False
skip_turn_player_two = False

for row in range(MATRIX_SIZE):
    matrix.append(input().split())


while True:
    player = player_1 if turn % 2 != 0 else player_2
    turn += 1



    row, col = input().strip('()').split(', ')
    row, col = int(row), int(col)

    if player == player_1 and skip_turn_player_one:
        skip_turn_player_one = False
        continue

    if player == player_2 and skip_turn_player_two:
        skip_turn_player_two = False
        continue

    if matrix[row][col] == 'E':
        print(f"{player} found the Exit and wins the game!")
        break

    elif matrix[row][col] == 'T':
        print(f"{player} is out of the game! The winner is {player_1 if player == player_2 else player_2}.")
        break

    elif matrix[row][col] == 'W':
        print(f"{player} hits a wall and needs to rest.")
        if player == player_1:
            skip_turn_player_one = True
        else:
            skip_turn_player_two = True


    elif matrix[row][col] == '.':
        continue


