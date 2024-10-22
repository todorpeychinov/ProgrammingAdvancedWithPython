from collections import deque

chocolate = list(map(int, input().split(', ')))
milk = deque(list(map(int, input().split(', '))))
total = 0

while chocolate and milk and total < 5:
    if chocolate[-1] <= 0 and milk[0] <= 0:
        chocolate.pop()
        milk.popleft()
        continue
    if chocolate[-1] <= 0:
        chocolate.pop()
        continue
    if milk[0] <= 0:
        milk.popleft()
        continue
    if chocolate[-1] == milk[0]:
        total += 1
        chocolate.pop()
        milk.popleft()
    else:
        milk.rotate(-1)
        chocolate[-1] -= 5

if total == 5:
    print('Great! You made all the chocolate milkshakes needed!')
else:
    print('Not enough milkshakes.')

print(f"Chocolate: {', '.join([str(choc) for choc in chocolate]) if chocolate else 'empty'}")
print(f"Milk: {', '.join([str(m) for m in milk]) if milk else 'empty'}")