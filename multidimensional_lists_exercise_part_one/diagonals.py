matrix = [[int(num) for num in input().split(', ')] for row in range(int(input()))]

primary_diagonal = []
secondary_diagonal = []

for i, j in zip(range(len(matrix)), range(len(matrix) - 1, -1, -1)):
    primary_diagonal.append(matrix[i][i])
    secondary_diagonal.append(matrix[i][j])

print(f"Primary diagonal: {', '.join(str(num) for num in primary_diagonal)}. Sum: {sum(primary_diagonal)}")
print(f"Secondary diagonal: {', '.join(str(num) for num in secondary_diagonal)}. Sum: {sum(secondary_diagonal)}")

