from collections import deque

customers = deque([int(el) for el in input().split(', ')])
taxis = [int(el) for el in input().split(', ')]

total_time = 0

while taxis and customers:
    customer = customers.popleft()
    taxi = taxis.pop()

    if taxi >= customer:
        total_time += customer

    else:
        customers.appendleft(customer)

if not customers:
    print(f"All customers were driven to their destinations\nTotal time: {total_time} minutes")
else:
    print('Not all customers were driven to their destinations\n'
          f'Customers left: {", ".join([str(el) for el in customers])}')