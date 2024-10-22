from collections import deque

firework_effects = deque([int(el) for el in input().split(', ')])
explosive_power = [int(el) for el in input().split(', ')]

fireworks = {
    "Palm Fireworks": 0,
    "Willow Fireworks": 0,
    "Crossette Fireworks": 0

}

needed_fireworks_ready = False

while firework_effects and explosive_power and not needed_fireworks_ready:

    if firework_effects[0] <= 0:
        firework_effects.popleft()
        continue

    if explosive_power[-1] <= 0:
        explosive_power.pop()
        continue


    effect = firework_effects.popleft()
    power = explosive_power.pop()

    sum_elements = effect + power

    if sum_elements % 3 == 0 and sum_elements % 5 != 0:
        fireworks["Palm Fireworks"] += 1


    elif sum_elements % 5 == 0 and sum_elements % 3 != 0:
        fireworks["Willow Fireworks"] += 1


    elif sum_elements % 3 == 0 and sum_elements % 5 == 0:
        fireworks["Crossette Fireworks"] += 1


    else:
        effect -= 1
        firework_effects.append(effect)
        explosive_power.append(power)

    if all(value >= 3 for value in fireworks.values()):
        needed_fireworks_ready = True


if needed_fireworks_ready:
    print("Congrats! You made the perfect firework show!")
else:
    print("Sorry. You can't make the perfect firework show.")

if firework_effects:
    print(f'Firework Effects left: {", ".join(str(el) for el in firework_effects)}')
if explosive_power:
    print(f'Explosive Power left: {", ".join(str(el) for el in explosive_power)}')

for el, count in fireworks.items():
    print(f"{el}: {count}")