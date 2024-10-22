from collections import deque


def calculate(bee, nectar, operator):
    if operator == '+':
        return abs(bee + nectar_amount)
    elif operator == '-':
        return abs(bee - nectar_amount)
    elif operator == '*':
        return abs(bee * nectar_amount)
    elif operator == '/':
        if nectar == 0:
            return 0
        return abs(bee / nectar_amount)
    else:
        return 0


bees = deque(list(map(int, input().split())))
nectar = list(map(int, input().split()))
operators = deque(input().split())
honey = 0

while bees and nectar:
    bee = bees[0]
    nectar_amount = nectar[-1]
    if nectar_amount >= bee:
        honey += calculate(bee, nectar_amount, operators.popleft())
        bees.popleft()
        nectar.pop()
    else:
        nectar.pop()

print(f"Total honey made: {honey}")

if bees:
    print(f"Bees left: {', '.join([str(bee) for bee in bees])}")
if nectar:
    print(f"Nectar left: {', '.join([str(nect) for nect in nectar])}")

