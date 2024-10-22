row_num, col_num = [int(num) for num in input().split(', ')]

matrix = []
total_sum = 0

for row in range(row_num):
    row_data = [int(num) for num in input().split(', ')]
    total_sum += sum(row_data)
    matrix.append(row_data)

print(total_sum)
print(matrix)


# for row in range(row_num):
#     matrix.append([])
#     row_data = [int(num) for num in input().split(', ')]
#     for col in range(col_num):
#         matrix[row].append(row_data[col])
#         total_sum += matrix[row][col]
# print(total_sum)
# print(matrix)
