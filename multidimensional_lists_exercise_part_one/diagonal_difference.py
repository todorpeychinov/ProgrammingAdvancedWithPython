matrix = [[int(num) for num in input().split()] for row in range(int(input()))]

primary_diagonal_sum = 0
secondary_diagonal_sum = 0

for i, j in zip(range(len(matrix)), range(len(matrix) - 1, -1, -1)):
    primary_diagonal_sum += matrix[i][i]
    secondary_diagonal_sum += matrix[i][j]

print(abs(primary_diagonal_sum - secondary_diagonal_sum))