from collections import deque


def calculate(num1, num2, operator):
    if operator == '+':
        return num1 + num2
    elif operator == '-':
        return num1 - num2
    elif operator == '*':
        return num1 * num2
    elif operator == '/':
        return num1 // num2



expression = input().split()
numbers = deque()

for character in expression:
    if character not in '+-/*':
        numbers.append(int(character))
    else:
        while len(numbers) > 1:
            num1 = numbers.popleft()
            num2 = numbers.popleft()
            numbers.appendleft(calculate(num1, num2, character))

print(numbers.popleft())

