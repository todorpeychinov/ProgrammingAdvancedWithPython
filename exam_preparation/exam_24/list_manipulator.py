from collections import deque


def list_manipulator(numbers, param, param_2, *args):
    if param == 'add':
        if param_2 == 'beginning':
            numbers = deque(numbers)
            for num in args[::-1]:
                numbers.appendleft(num)
            return list(numbers)
        elif param_2 == 'end':
            for num in args:
                numbers.append(num)
            return numbers
    elif param == 'remove':
        if param_2 == 'beginning':
            numbers = deque(numbers)
            if args:
                count = args[0]
                for _ in range(count):
                    numbers.popleft()
                return list(numbers)
            else:
                numbers.popleft()
                return list(numbers)
        elif param_2 == 'end':
            if args:
                count = args[0]
                for _ in range(count):
                    numbers.pop()
                return numbers
            else:
                numbers.pop()
                return numbers

print(list_manipulator([1,2,3], "remove", "end"))
print(list_manipulator([1,2,3], "remove", "beginning"))
print(list_manipulator([1,2,3], "add", "beginning", 20))
print(list_manipulator([1,2,3], "add", "end", 30))
print(list_manipulator([1,2,3], "remove", "end", 2))
print(list_manipulator([1,2,3], "remove", "beginning", 2))
print(list_manipulator([1,2,3], "add", "beginning", 20, 30, 40))
print(list_manipulator([1,2,3], "add", "end", 30, 40, 50))


