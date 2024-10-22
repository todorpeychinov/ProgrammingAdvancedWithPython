from collections import deque


def check_color(c, list_of_colors):
    if c == 'orange' and 'red' in list_of_colors and 'yellow' in list_of_colors:
        return True
    elif c == 'purple' and 'red' in list_of_colors and 'blue' in list_of_colors:
        return True
    elif c == 'green' and 'yellow' in list_of_colors and 'blue' in list_of_colors:
        return True
    elif c == 'red' or c == 'yellow' or c == 'blue':
        return True
    else:
        return False


user_input = deque(input().split())
colors = ["red", "yellow", "blue", "orange", "purple", "green"]

founded_colors = []

while user_input:
    first = user_input.popleft()
    last = user_input.pop() if user_input else ''

    for c in (first + last, last + first):
        if c in colors:
            founded_colors.append(c)
            break
    else:
        if len(first) > 1:
            user_input.insert(len(user_input) // 2, first[:-1])
        if len(last) > 1:
            user_input.insert(len(user_input) // 2, last[:-1])


for c in founded_colors:
    if not check_color(c, founded_colors):
        founded_colors.remove(c)

print(founded_colors)
