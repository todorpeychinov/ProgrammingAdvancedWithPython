from collections import deque

pumps = deque()

number_of_pumps = int(input())

for _ in range(number_of_pumps):
    petrol_amount, distance = input().split()
    petrol_amount = int(petrol_amount)
    distance = int(distance)
    pumps.append([petrol_amount, distance])

start_pump = 0
tank = 0

while True:
    for pump in pumps:
        tank += pump[0]
        distance = pump[1]
        if tank < distance:
            start_pump += 1
            tank = 0
            pumps.rotate(-1)
            break
        else:
            tank -= distance
    else:
        break


print(start_pump)


