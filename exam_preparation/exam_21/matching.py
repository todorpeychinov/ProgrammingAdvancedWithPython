from collections import deque

males = [int(el) for el in input().split()]
females = deque([int(el) for el in input().split()])
matches = 0

while males and females:

    if males[-1] <= 0:
        males.pop()
        continue

    if females[0] <= 0:
        females.popleft()
        continue

    if males[-1] % 25 == 0:
        males.pop()
        males.pop()
        continue

    if females[0] % 25 == 0:
        females.popleft()
        females.popleft()
        continue

    male = males.pop()
    female = females.popleft()

    if male == female:
        matches += 1

    else:
        males.append((male - 2))

print(f"Matches: {matches}")
print(f'Males left: {", ".join(map(str, males[::-1])) if males else "none"}')
print(f'Females left: {", ".join(map(str, females)) if females else "none"}')







