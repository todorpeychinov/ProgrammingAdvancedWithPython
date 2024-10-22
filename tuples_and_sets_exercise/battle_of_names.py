even_numbers_set = set()
odd_numbers_set = set()

for row in range(1, int(input()) + 1):
    name = input()
    current_result = sum([ord(ch) for ch in name]) // row

    if current_result % 2 == 0:
        even_numbers_set.add(current_result)
    else:
        odd_numbers_set.add(current_result)

sum_even_numbers_set = sum(even_numbers_set)
sum_odd_numbers_set = sum(odd_numbers_set)

if sum_even_numbers_set == sum_odd_numbers_set:
    print(*(even_numbers_set.union(odd_numbers_set)), sep=', ')
elif sum_odd_numbers_set > sum_even_numbers_set:
    print(*(odd_numbers_set.difference(even_numbers_set)), sep=', ')
else:
    print(*(even_numbers_set.symmetric_difference(odd_numbers_set)), sep=', ')


