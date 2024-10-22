rows_num = int(input())
matrix = []
diagonal_sum = 0

for row in range(rows_num):
    row_data = [int(num) for num in input().split()]
    matrix.append(row_data)

for index in range(rows_num):
    diagonal_sum += matrix[index][index]

print(diagonal_sum)

