number_of_commands = int(input())

cars_register = set()

for _ in range(number_of_commands):
    direction, car_number = input().split(', ')

    if direction == 'IN':
        cars_register.add(car_number)

    elif direction == 'OUT':
        if cars_register:
            cars_register.remove(car_number)


if cars_register:
    for car in cars_register:
        print(car)
else:
    print("Parking Lot is Empty")