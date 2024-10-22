from collections import deque

required_strength = [int(el) for el in input().split()]
accuracy_needed = deque([int(el) for el in input().split()])
total_goals = 0

while required_strength and accuracy_needed:
    current_strength = required_strength.pop()
    current_accuracy = accuracy_needed.popleft()

    result = current_strength + current_accuracy

    if result == 100:
        total_goals += 1

    elif result < 100:
        if current_strength < current_accuracy:
            accuracy_needed.appendleft(current_accuracy)
        elif current_strength > current_accuracy:
            required_strength.append(current_strength)
        else:
            required_strength.append(result)

    else:
        current_strength -= 10
        required_strength.append(current_strength)
        accuracy_needed.append(current_accuracy)


if total_goals == 3:
    print("Paul scored a hat-trick!")

elif total_goals == 0:
    print("Paul failed to score a single goal.")

elif total_goals > 3:
    print("Paul performed remarkably well!")

elif 0 < total_goals < 3:
    print("Paul failed to make a hat-trick.")


if total_goals > 0:
    print(f"Goals scored: {total_goals}")

if required_strength:
    print(f'Strength values left: {", ".join(str(el) for el in required_strength)}')

if accuracy_needed:
    print(f'Accuracy values left: {", ".join(str(el) for el in accuracy_needed)}')