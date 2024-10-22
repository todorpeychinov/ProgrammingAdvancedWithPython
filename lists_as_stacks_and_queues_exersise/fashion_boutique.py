clothes_stack = list(map(int, input().split()))
rack_capacity = int(input())
racks_num = 0

current_rack_space = rack_capacity
racks_num += 1

while clothes_stack:
    current_clothes_weight = clothes_stack[-1]

    if current_clothes_weight > current_rack_space:
        current_rack_space = rack_capacity
        racks_num += 1
        continue
    else:
        clothes_stack.pop()
        current_rack_space -= current_clothes_weight

print(racks_num)

