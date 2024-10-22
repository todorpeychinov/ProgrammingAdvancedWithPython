n = int(input())

matrix = [[int(num) for num in input().split()] for _ in range(n)]

while True:
    command = input().split()

    if command[0] == 'END':
        break

    row = int(command[1])
    col = int(command[2])
    value = int(command[3])

    if 0 <= row < n and 0 <= col < n:
        if command[0] == 'Add':
            matrix[row][col] += value
        elif command[0] == 'Subtract':
            matrix[row][col] -= value
    else:
        print('Invalid coordinates')
        continue

[print(*row) for row in matrix]
