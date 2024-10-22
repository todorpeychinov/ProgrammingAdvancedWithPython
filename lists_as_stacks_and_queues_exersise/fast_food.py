from collections import deque

food_quantity = int(input())
orders: deque[int] = deque(list(map(int, input().split())))

print(max(orders))

while orders:
    current_order = orders[0]
    if current_order <= food_quantity:
        orders.popleft()
        food_quantity -= current_order
    else:
        break

if orders:
    print(f"Orders left: ", end='')
    print(*orders)
else:
    print('Orders complete')
