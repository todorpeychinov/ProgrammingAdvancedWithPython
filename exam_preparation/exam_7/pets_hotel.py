def accommodate_new_pets(capacity, maximum_weight, *args):
    available_capacity = capacity
    pets = {}
    result = ''
    for pet_type, pet_weight in args:
        if available_capacity > 0:
            if pet_weight > maximum_weight:
                continue
            if pet_type not in pets:
                pets[pet_type] = 0
            pets[pet_type] += 1
            available_capacity -= 1
        else:
            result += "You did not manage to accommodate all pets!\n"
            break
    else:
        result += f"All pets are accommodated! Available capacity: {available_capacity}.\n"

    result += 'Accommodated pets:\n'

    for pet_type, count in sorted(pets.items()):
        result += f"{pet_type}: {count}\n"

    return result.strip()

print(accommodate_new_pets(
    10,
    15.0,
    ("cat", 5.8),
    ("dog", 10.0),
))

print(accommodate_new_pets(
    10,
    10.0,
    ("cat", 5.8),
    ("dog", 10.5),
    ("parrot", 0.8),
    ("cat", 3.1),
))

print(accommodate_new_pets(
    2,
    15.0,
    ("dog", 10.0),
    ("cat", 5.8),
    ("cat", 2.7),
))




