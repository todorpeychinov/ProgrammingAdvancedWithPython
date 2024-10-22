from collections import deque

green_light_duration = int(input())
free_window = int(input())

total_cars = 0
cars = deque()

while True:
    command = input()
    if command == 'END':
        break

    elif command == 'green':
        current_green_time = green_light_duration

        while current_green_time > 0 and cars:
            car = cars.popleft()
            if len(car) > current_green_time + free_window:
                print(f"A crash happened!")
                print(f"{car} was hit at {car[current_green_time + free_window]}.")
                raise SystemExit
            else:
                current_green_time -= len(car)
                total_cars += 1
    else:
        cars.append(command)

print("Everyone is safe.")
print(f"{total_cars} total cars passed the crossroads.")
