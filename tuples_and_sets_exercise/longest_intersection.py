longest_intersection = []

number_of_inputs = int(input())

for _ in range(number_of_inputs):
    range_a, range_b = input().split('-')
    start_a, end_a = map(int, range_a.split(','))
    start_b, end_b = map(int, range_b.split(','))

    set_a = set([int(num) for num in range(start_a, end_a + 1)])
    set_b = set([int(num) for num in range(start_b, end_b + 1)])

    intersection = set_a.intersection(set_b)

    if len(intersection) > len(longest_intersection):
        longest_intersection = intersection

print(f'Longest intersection is {list(longest_intersection)} with length {len(longest_intersection)}')
