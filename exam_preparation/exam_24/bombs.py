from collections import deque

bomb_effects = deque([int(el) for el in input().split(', ')])
bomb_casings = [int(el) for el in input().split(', ')]

bombs = {
    "Cherry Bombs": 0,
    "Datura Bombs": 0,
    "Smoke Decoy Bombs": 0
}

while bomb_casings and bomb_effects:
    effect = bomb_effects.popleft()
    casing = bomb_casings.pop()

    bomb_sum = casing + effect

    if bomb_sum == 40:
        bombs["Datura Bombs"] += 1

    elif bomb_sum == 60:
        bombs["Cherry Bombs"] += 1

    elif bomb_sum == 120:
        bombs["Smoke Decoy Bombs"] += 1

    else:
        casing -= 5
        bomb_effects.appendleft(effect)
        bomb_casings.append(casing)

    if all([value >= 3 for value in bombs.values()]):
        print("Bene! You have successfully filled the bomb pouch!")
        break
else:
    print("You don't have enough materials to fill the bomb pouch.")

print(f'Bomb Effects: {", ".join(map(str, bomb_effects)) if bomb_effects else "empty"}')
print(f'Bomb Casings: {", ".join(map(str, bomb_casings)) if bomb_casings else "empty"}')

for k, v in bombs.items():
    print(f"{k}: {v}")