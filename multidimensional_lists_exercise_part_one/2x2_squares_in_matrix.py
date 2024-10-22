rows, cols = [int(num) for num in input().split()]

matrix = [[ch for ch in input().split()] for row in range(rows)]
total_identical = 0

for row in range(rows - 1):
    for col in range(cols - 1):
        upper = matrix[row][col]
        upper_right = matrix[row][col + 1]
        lower = matrix[row + 1][col]
        lower_right = matrix[row + 1][col + 1]
        if upper == upper_right == lower == lower_right:
            total_identical += 1

print(total_identical)
