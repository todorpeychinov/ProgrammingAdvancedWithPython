from collections import deque

cups = deque(list(map(int, input().split())))
bottles = deque(list(map(int, input().split())))
wasted_water = 0

while bottles and cups:
    current_bottle = bottles.pop()
    current_cup = cups[0]

    if current_bottle >= current_cup:
        cups.popleft()
        wasted_water += current_bottle - current_cup
    else:
        cups[0] -= current_bottle

if not cups:
    print(f'Bottles: {" ".join([str(current_bottle) for current_bottle in bottles])}')

if not bottles:
    print(f'Cups: {" ".join([str(current_cup) for current_cup in cups])}')

print(f"Wasted litters of water: {wasted_water}")



