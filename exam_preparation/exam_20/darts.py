MATRIX_SIZE = 7

player_1_score = 501
player_2_score = 501
matrix = []

player_1_name, player_2_name = input().split(', ')

players = {
    player_1_name: {'score': player_1_score, 'throws': 0},
    player_2_name: {'score': player_2_score, 'throws': 0}
}

turn = 1

for row in range(MATRIX_SIZE):
    matrix.append(input().split())

while True:

    player = player_1_name if turn % 2 != 0 else player_2_name
    players[player]['throws'] += 1
    turn += 1

    row, col = map(int, input().strip('()').split(', '))

    if not (0 <= row < MATRIX_SIZE and 0 <= col < MATRIX_SIZE):
        continue

    if matrix[row][col].isdigit():
        players[player]['score'] -= int(matrix[row][col])

    elif matrix[row][col] == 'D':
        scored_points = (int(matrix[row][0]) + int(matrix[row][-1]) + int(matrix[0][col]) + int(matrix[-1][col])) * 2
        players[player]['score'] -= scored_points

    elif matrix[row][col] == 'T':
        scored_points = (int(matrix[row][0]) + int(matrix[row][-1]) + int(matrix[0][col]) + int(matrix[-1][col])) * 3
        players[player]['score'] -= scored_points

    elif matrix[row][col] == 'B':
        print(f"{player} won the game with {players[player]['throws']} throws!")
        break

    if players[player]['score'] <= 0:
        print(f"{player} won the game with {players[player]['throws']} throws!")
        break








