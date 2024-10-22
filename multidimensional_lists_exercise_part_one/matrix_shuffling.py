rows, cols = [int(num) for num in input().split()]

matrix = [[el for el in input().split()] for _ in range(rows)]

commands = ['END', 'swap']

while True:
    command = input().split()
    cmd = command[0]
    if cmd == 'END':
        break
    elif cmd not in commands or len(command) > 5:
        print("Invalid input!")
        continue
    elif cmd == 'swap':
        start_idx = int(command[1])
        end_idx = int(command[2])
        start_idx_swap = int(command[3])
        end_idx_swap = int(command[4])
        if 0 <= start_idx < rows and 0 <= end_idx < cols and 0 <= start_idx_swap < rows and 0 <= end_idx_swap < cols:
            matrix[start_idx][end_idx], matrix[start_idx_swap][end_idx_swap] = matrix[start_idx_swap][end_idx_swap], matrix[start_idx][end_idx]
            [print(*row_data) for row_data in matrix]
        else:
            print("Invalid input!")