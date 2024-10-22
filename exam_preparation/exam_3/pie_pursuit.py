from collections import deque

contestant = deque([int(el) for el in input().split()])
pies = [int(el) for el in input().split()]

while pies and contestant:
    current_contestant = contestant.popleft()
    current_pie = pies.pop()

    if current_contestant >= current_pie:
        current_contestant -= current_pie
        if current_contestant > 0:
            contestant.append(current_contestant)
    else:
        current_pie -= current_contestant

        if current_pie > 1:
            pies.append(current_pie)
        elif current_pie == 1:
            if len(pies) > 1:
                pies[-1] += 1
            else:
                pies.append(1)


if not pies and contestant:
    print("We will have to wait for more pies to be baked!")
    print(f'Contestants left: {", ".join(str(el) for el in contestant)}')

elif not pies and not contestant:
    print("We have a champion!")

else:
    print("Our contestants need to rest!")
    print(f'Pies left: {", ".join(str(el) for el in pies)}')

