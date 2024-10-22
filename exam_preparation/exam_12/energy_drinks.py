from collections import deque

caffeine_milligrams = [int(el) for el in input().split(', ')]
energy_drinks = deque(int(el) for el in input().split(', '))

caffeine = 0
MAX_AMOUNT_OF_CAFFEINE = 300

while caffeine_milligrams and energy_drinks:
    milligrams = caffeine_milligrams.pop()
    drink = energy_drinks.popleft()

    result = milligrams * drink

    if result + caffeine <= MAX_AMOUNT_OF_CAFFEINE:
        caffeine += result
    else:
        energy_drinks.append(drink)
        caffeine -= 30
        if caffeine < 0:
            caffeine = 0

if energy_drinks:
    print(f'Drinks left: {", ".join(str(el) for el in energy_drinks)}')
else:
    print("At least Stamat wasn't exceeding the maximum caffeine.")

print(f"Stamat is going to sleep with {caffeine} mg caffeine.")