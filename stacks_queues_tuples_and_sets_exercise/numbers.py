set_a = set(map(int, input().split()))
set_b = set(map(int, input().split()))

n = int(input())

for _ in range(n):
    user_input = input().split()
    cmd = f'{user_input[0]} {user_input[1]}'
    numbers = [int(num) for num in user_input[2:]]

    if cmd == 'Add First':
        set_a.update(numbers)
    elif cmd == 'Add Second':
        set_b.update(numbers)
    elif cmd == 'Remove First':
        set_a.difference_update(numbers)
    elif cmd == 'Remove Second':
        set_b.difference_update(numbers)
    elif cmd == 'Check Subset':
        print(set_a.issubset(set_b) or set_b.issubset(set_a))

print(*sorted(set_a), sep=', ')
print(*sorted(set_b), sep=', ')