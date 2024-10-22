from collections import deque

packages = [int(el) for el in input().split()]
couriers = deque([int(el) for el in input().split()])
delivered_packages = 0

while packages and couriers:
    current_package = packages.pop()
    current_courier_capacity = couriers.popleft()

    if current_courier_capacity >= current_package:
        delivered_packages += current_package
        if current_courier_capacity > current_package:
            current_courier_capacity -= current_package * 2
            if current_courier_capacity > 0:
                couriers.append(current_courier_capacity)
    else:
        current_package -= current_courier_capacity
        packages.append(current_package)
        delivered_packages += current_courier_capacity

print(f"Total weight: {delivered_packages} kg")

if not packages and not couriers:
    print("Congratulations, all packages were delivered successfully by the couriers today.")

if packages and not couriers:
    print(f'Unfortunately, there are no more available couriers to deliver the following packages: {", ".join(str(el) for el in packages)}')

if not packages and couriers:
    print(f'Couriers are still on duty: {", ".join(str(el) for el in couriers)} but there are no more packages to deliver.')