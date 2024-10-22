rows_number = int(input())
matrix = []

for row in range(rows_number):
    row_data = [int(num) for num in input().split(', ') if int(num) % 2 == 0]
    matrix.append(row_data)

print(matrix)
