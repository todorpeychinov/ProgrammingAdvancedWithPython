rows_count = int(input())
matrix = []

for row in range(rows_count):
    row_data = list(input())
    matrix.append(row_data)

symbol = input()

for row in range(rows_count):
    for col in range(len(matrix[row])):
        if matrix[row][col] == symbol:
            symbol_position = (row, col)
            print(symbol_position)
            exit()

print(f"{symbol} does not occur in the matrix")
