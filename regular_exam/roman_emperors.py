def list_roman_emperors(*args, **kwargs):
    successful_emperors = {}
    unsuccessful_emperors = {}

    for name, status in args:
        if status:
            successful_emperors[name] = None
        else:
            unsuccessful_emperors[name] = None

    for k, v in kwargs.items():
        if k in successful_emperors:
            successful_emperors[k] = v
        else:
            unsuccessful_emperors[k] = v
    if successful_emperors:
        sorted_successful_emperors = sorted(successful_emperors.items(), key=lambda x: (-x[1], x[0]))

    if unsuccessful_emperors:
        sorted_unsuccessful_emperors = sorted(unsuccessful_emperors.items(), key=lambda x: (x[1], x[0]))

    result = ''

    result += f"Total number of emperors: {len(successful_emperors) + len(unsuccessful_emperors)}\n"

    if successful_emperors:
        result += "Successful emperors:\n"
        for name, years in sorted_successful_emperors:
            result += f"****{name}: {years}\n"

    if unsuccessful_emperors:
        result += "Unsuccessful emperors:\n"
        for name, years in sorted_unsuccessful_emperors:
            result += f"****{name}: {years}\n"

    return result.strip()



print(list_roman_emperors(("Augustus", True), ("Nero", False), Augustus=40, Nero=14,))
print()
print(list_roman_emperors(("Augustus", True), ("Trajan", True), ("Nero", False), ("Caligula", False), ("Pertinax", False), ("Vespasian", True), Augustus=40, Trajan=19, Nero=14, Caligula=4, Pertinax=4, Vespasian=19,))
print()
print(list_roman_emperors(("Augustus", True), ("Trajan", True), ("Claudius", True), Augustus=40, Trajan=19, Claudius=13,))