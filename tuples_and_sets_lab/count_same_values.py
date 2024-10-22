numbers = tuple(input().split())
occurences = {}

for num in numbers:
    occurences[num] = numbers.count(num)

for num, count in occurences.items():
    print(f"{float(num):.1f} - {count} times")