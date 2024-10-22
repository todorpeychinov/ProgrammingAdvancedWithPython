def check_range(r, c, m_size):
    if 0 <= r < m_size and 0 <= c < m_size:
        return True
    return False


def calc_number(row, col, n, m):
    num = 0
    if check_range(row - 1, col - 1, n):
        if m[row - 1][col - 1] == '*':
            num += 1
    if check_range(row - 1, col, n):
        if m[row - 1][col] == '*':
            num += 1
    if check_range(row - 1, col + 1, n):
        if m[row - 1][col + 1] == '*':
            num += 1
    if check_range(row, col - 1, n):
        if m[row][col - 1] == '*':
            num += 1
    if check_range(row, col + 1, n):
        if m[row][col + 1] == '*':
            num += 1
    if check_range(row + 1, col - 1, n):
        if m[row + 1][col - 1] == '*':
            num += 1
    if check_range(row + 1, col, n):
        if m[row + 1][col] == '*':
            num += 1
    if check_range(row + 1, col + 1, n):
        if m[row + 1][col + 1] == '*':
            num += 1
    return num


n = int(input())
matrix = []

for row in range(n):
    matrix.append([])
    for col in range(n):
        matrix[row].append([])

bombs_num = int(input())

for _ in range(bombs_num):
    row, col = map(int, input().strip('()').split(', '))
    matrix[row][col] = '*'

for row in range(n):
    for col in range(n):
        if not matrix[row][col]:
            number = calc_number(row, col, n, matrix)
            matrix[row][col] = number


[print(*row) for row in matrix]
