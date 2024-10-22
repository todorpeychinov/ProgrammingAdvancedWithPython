from collections import deque

programmers_times = deque(int(el) for el in input().split())
tasks_number = [int(el) for el in input().split()]

ducks = {'Darth Vader Ducky': 0,
         'Thor Ducky': 0,
         'Big Blue Rubber Ducky': 0,
         'Small Yellow Rubber Ducky': 0}

while programmers_times and tasks_number:
    time = programmers_times.popleft()
    tasks = tasks_number.pop()

    time_needed = time * tasks

    if 0 <= time_needed <= 60:
        ducks['Darth Vader Ducky'] += 1
        continue
    elif 61 <= time_needed <= 120:
        ducks['Thor Ducky'] += 1
        continue
    elif 121 <= time_needed <= 180:
        ducks['Big Blue Rubber Ducky'] += 1
        continue
    elif 181 <= time_needed <= 240:
        ducks['Small Yellow Rubber Ducky'] += 1
        continue
    elif time_needed > 240:
        tasks -= 2
        tasks_number.append(tasks)
        programmers_times.append(time)
        continue
    else:
        programmers_times.appendleft(time)
        tasks_number.append(tasks)

print("Congratulations, all tasks have been completed! Rubber ducks rewarded:")
print(f"Darth Vader Ducky: {ducks['Darth Vader Ducky']}\n"
      f"Thor Ducky: {ducks['Thor Ducky']}\n"
      f"Big Blue Rubber Ducky: {ducks['Big Blue Rubber Ducky']}\n"
      f"Small Yellow Rubber Ducky: {ducks['Small Yellow Rubber Ducky']}")




