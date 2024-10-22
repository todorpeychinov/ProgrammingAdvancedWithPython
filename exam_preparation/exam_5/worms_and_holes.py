from collections import deque

worms = [int(el) for el in input().split()]
holes = deque([int(el) for el in input().split()])
matches = 0
every_fitted = True

while worms and holes:
    worm = worms.pop()
    hole = holes.popleft()

    if worm == hole:
        matches += 1
        continue
    else:
        every_fitted = False
        worm -= 3
        if worm > 0:
            worms.append(worm)


if matches > 0:
    print(f"Matches: {matches}")
else:
    print("There are no matches.")

if not worms:
    if every_fitted:
        print("Every worm found a suitable hole!")
    else:
        print("Worms left: none")
else:
    print(f'Worms left: {", ".join(str(el) for el in worms)}')

if not holes:
    print("Holes left: none")
else:
    print(f'Holes left: {", ".join(str(hole) for hole in holes)}')

