from collections import deque

def best_list_pureness(numbers, number):
    best_pureness = float("-inf")
    rotation = None
    numbers = deque(numbers)
    for i in range(1, number + 1):
        current_sum = 0
        for index, number in enumerate(numbers):
            current_sum += (number * index)
        if current_sum > best_pureness:
            best_pureness = current_sum
            rotation = i - 1
        numbers.rotate(1)
    return f"Best pureness {best_pureness} after {rotation} rotations"

test = ([4, 3, 2, 6], 4)
result = best_list_pureness(*test)
print(result)
test = ([7, 9, 2, 5, 3, 4], 3)
result = best_list_pureness(*test)
print(result)
test = ([1, 2, 3, 4, 5], 10)
result = best_list_pureness(*test)
print(result)
