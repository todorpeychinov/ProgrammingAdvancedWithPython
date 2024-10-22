from collections import deque

bees = deque((map(int, input().split())))
bee_eaters = list(map(int, input().split()))

while bees and bee_eaters:
    current_bee_group = bees.popleft()
    current_bee_eater_group = bee_eaters.pop()

    while current_bee_group > 0 and current_bee_eater_group > 0:
        current_bee_group -= 7
        current_bee_eater_group -= 1

    if current_bee_group < 0:
        current_bee_eater_group += 1

    if current_bee_eater_group > 0 >= current_bee_group:
        bee_eaters.append(current_bee_eater_group)

    elif current_bee_group > 0 >= current_bee_eater_group:
        bees.append(current_bee_group)

print("The final battle is over!")

if not bee_eaters and not bees:
    print("But no one made it out alive!")

if bees:
    print(f'Bee groups left: {", ".join([str(bee) for bee in bees])}')

if bee_eaters:
    print(f'Bee-eater groups left: {", ".join(str(bee_eater) for bee_eater in bee_eaters)}')








