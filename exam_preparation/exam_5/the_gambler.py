def check_matrix_boundaries(x, y, matrix_size):
    if x < 0 or x >= matrix_size or y < 0 or y >= matrix_size:
        return False
    return True


directions = {'up': (-1, 0), 'down': (1, 0), 'left': (0, -1), 'right': (0, 1)}
gambler_position = None
matrix = []
money = 100

n = int(input())

for row in range(n):
    matrix.append(list(input()))
    for col in range(n):
        if matrix[row][col] == 'G':
            gambler_position = [row, col]
            matrix[row][col] = '-'

while True:
    direction = input()

    if direction == "end":
        print(f"End of the game. Total amount: {money}$")
        break

    next_row, next_col = gambler_position[0] + directions[direction][0], gambler_position[1] + directions[direction][1]

    if check_matrix_boundaries(next_row, next_col, n):
        gambler_position = [next_row, next_col]

        if matrix[next_row][next_col] == '-':
            continue

        elif matrix[next_row][next_col] == 'W':
            money += 100
            matrix[next_row][next_col] = '-'

        elif matrix[next_row][next_col] == 'P':
            money -= 200
            matrix[next_row][next_col] = '-'
            if money <= 0:
                print("Game over! You lost everything!")
                break

        elif matrix[next_row][next_col] == 'J':
            money += 100000
            print(f"You win the Jackpot!\nEnd of the game. Total amount: {money}$")
            break

    else:
        print("Game over! You lost everything!")
        break


matrix[gambler_position[0]][gambler_position[1]] = 'G'
if money > 0:
    [print(*row, sep='') for row in matrix]