from collections import deque

pizza_orders = deque([int(el) for el in input().split(', ')])
employees_capacity = [int(el) for el in input().split(', ')]

pizzas_made = 0

while pizza_orders and employees_capacity:
    order = pizza_orders.popleft()

    if order > 10 or order <= 0:
        continue

    capacity = employees_capacity.pop()

    if order <= capacity:
        pizzas_made += order

    elif order > capacity:
        if employees_capacity:
            remaining = order - capacity
            pizzas_made += capacity
            pizza_orders.appendleft(remaining)
        else:
            remaining = order - capacity
            pizza_orders.appendleft(remaining)



if not pizza_orders:
    print("All orders are successfully completed!")
    print(f"Total pizzas made: {pizzas_made}")
    print(f'Employees: {", ".join(str(el) for el in employees_capacity)}')

elif not employees_capacity:
    print("Not all orders are completed.")
    print(f'Orders left: {", ".join(str(el) for el in pizza_orders)}')