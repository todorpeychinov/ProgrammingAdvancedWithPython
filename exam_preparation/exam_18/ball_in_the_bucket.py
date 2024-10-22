MATRIX_SIZE = 6
matrix = []
score = 0
prize = None

for row in range(MATRIX_SIZE):
    matrix.append(input().split())


for _ in range(3):
    row, col = map(int, input().strip('()').split(', '))
    current_score = 0

    if 0 <= row < MATRIX_SIZE and 0 <= col < MATRIX_SIZE:
        if matrix[row][col] == 'B':
            matrix[row][col] = '-'
            for i in range(MATRIX_SIZE):
                if matrix[i][col].isdigit():
                    current_score += int(matrix[i][col])
            score += current_score


if score >= 300:
    prize = "Lego Construction Set"
elif score >= 200:
    prize = "Teddy Bear"
elif score >= 100:
    prize = "Football"

if prize:
    print(f"Good job! You scored {score} points, and you've won {prize}.")
else:
    print(f"Sorry! You need {100 - score} points more to win a prize.")



