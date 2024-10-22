row_count, col_count = [int(num) for num in input().split(', ')]

matrix = []
submatrix = []
max_sum = float('-inf')

for row in range(row_count):
    row_data = [int(num) for num in input().split(', ')]
    matrix.append(row_data)

for row in range(row_count - 1):
    for col in range(col_count - 1):
        current_upper = matrix[row][col]
        current_lower = matrix[row + 1][col]
        upper_right = matrix[row][col + 1]
        lower_right = matrix[row + 1][col + 1]
        current_sum = current_upper + current_lower + upper_right + lower_right
        if max_sum < current_sum:
            max_sum = current_sum
            submatrix = [[current_upper, upper_right], [current_lower, lower_right]]

print(*submatrix[0])
print(*submatrix[1])
print(max_sum)

