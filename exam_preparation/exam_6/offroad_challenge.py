from collections import deque

initial_fuel = [int(el) for el in input().split()]
indexes = deque([int(el) for el in input().split()])
fuel_needed = deque([int(el) for el in input().split()])
altitude = 0

while initial_fuel and indexes and fuel_needed:
    altitude += 1
    fuel = initial_fuel.pop()
    index = indexes.popleft()
    needed_fuel = fuel_needed.popleft()
    result = fuel - index

    if result >= needed_fuel:
        print(f"John has reached: Altitude {altitude}")
        continue
    else:
        fuel_needed.appendleft(needed_fuel)
        print(f"John did not reach: Altitude {altitude}")
        break


if fuel_needed and altitude > 1:
    print("John failed to reach the top.")
    print(f'Reached altitudes: {", ".join(f"Altitude {i}" for i in range(1, altitude))}')

if fuel_needed and altitude <= 1:
    print("John failed to reach the top.")
    print("John didn't reach any altitude.")

if not fuel_needed:
    print("John has reached all the altitudes and managed to reach the top!")
