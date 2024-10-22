rows_num, col_num = [int(num) for num in input().split(', ')]
matrix = []

for row in range(rows_num):
    row_data = [int(num) for num in input().split()]
    matrix.append(row_data)

for col in range(col_num):
    current_col_sum = 0
    for row in range(rows_num):
        current_col_sum += matrix[row][col]
    print(current_col_sum)
