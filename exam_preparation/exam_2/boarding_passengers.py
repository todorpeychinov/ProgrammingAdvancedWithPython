def boarding_passengers(capacity, *args):
    passengers_dictionary = {}
    waiting_guests = list(args)
    result = ""
    for passengers, benefit_program in args:

        if capacity == 0:
            break

        if capacity >= passengers:
            if benefit_program not in passengers_dictionary:
                passengers_dictionary[benefit_program] = 0
            passengers_dictionary[benefit_program] += passengers
            capacity -= passengers
            waiting_guests.remove((passengers, benefit_program))

    sorted_passengers = sorted(passengers_dictionary.items(), key=lambda x: (-x[1], x[0]))
    result += f"Boarding details by benefit plan:\n"

    for program, passengers_count in sorted_passengers:
        result += f"## {program}: {passengers_count} guests\n"

    if not waiting_guests:
        result += "All passengers are successfully boarded!"

    elif waiting_guests and capacity == 0:
        result += "Boarding unsuccessful. Cruise ship at full capacity."

    elif waiting_guests and capacity > 0:
        result += f"Partial boarding completed. Available capacity: {capacity}."

    return result


print(boarding_passengers(150, (35, 'Diamond'), (55, 'Platinum'), (35, 'Gold'), (25, 'First Cruiser')))
print()
print(boarding_passengers(100, (20, 'Diamond'), (15, 'Platinum'), (25, 'Gold'), (25, 'First Cruiser'), (15, 'Diamond'), (10, 'Gold')))
print()
print(boarding_passengers(120, (30, 'Gold'), (20, 'Platinum'), (30, 'Diamond'), (10, 'First Cruiser'), (31, 'Platinum'), (20, 'Diamond')))