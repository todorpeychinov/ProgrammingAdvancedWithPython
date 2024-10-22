def numbers_searching(*args):
    duplicated_numbers = []
    missing_number = None
    max_num, min_num = max(args), min(args)
    for num in range(min_num, max_num + 1):
        if num not in args:
            missing_number = num

    for num in args:
        if args.count(num) > 1 and num not in duplicated_numbers:
            duplicated_numbers.append(num)

    duplicated_numbers.sort()

    result = [missing_number, duplicated_numbers]
    return result


print(numbers_searching(1, 2, 4, 2, 5, 4))
print(numbers_searching(5, 5, 9, 10, 7, 8, 7, 9))
print(numbers_searching(50, 50, 47, 47, 48, 45, 49, 44, 47, 45, 44, 44, 48, 44, 48))

