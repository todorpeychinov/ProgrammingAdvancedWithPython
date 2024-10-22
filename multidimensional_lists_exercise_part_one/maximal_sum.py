rows, cols = [int(num) for num in input().split()]

matrix = [[int(num) for num in input().split()] for _ in range(rows)]
submatrix = []
max_sum = float('-inf')

for row in range(rows - 2):
    for col in range(cols - 2):
        current_sum = 0
        for i in range(row, row + 3):
            for j in range(col, col + 3):
                current_sum += matrix[i][j]
        if current_sum > max_sum:
            max_sum = current_sum
            submatrix = [k[col:col+3] for k in matrix[row:row+3]]

print(f"Sum = {max_sum}")
[print(*data) for data in submatrix]



