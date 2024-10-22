rows_num = int(input())
matrix = []


for row in range(rows_num):
    row_data = [int(num) for num in input().split(', ')]
    matrix.extend(row_data)

print(matrix)

# for row in range(rows_num):
#     row_data = [int(num) for num in input().split(', ')]
#     matrix.append(row_data)
#
# flattened_matrix = [num for row in matrix for num in row]
# 
# print(flattened_matrix)
