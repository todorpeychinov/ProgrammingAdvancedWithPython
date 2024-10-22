def naughty_or_nice_list(kids_list, *args, **kwargs):
    kids_dict = {
        "Nice": [],
        "Naughty": [],
        "Not found": []
    }

    for arg in args:
        idx, kid_type = arg.split('-')
        idx = int(idx)
        counter = 0
        current_name = None
        for current_idx, name in kids_list:
            if current_idx == idx:
                counter += 1
                current_name = name

        if counter == 1:
            kids_dict[kid_type].append(current_name)
            kids_list.remove((idx, current_name))

    for name, kid_type in kwargs.items():
        counter = 0
        idx = None
        for current_idx, curr_name in kids_list:
            if name == curr_name:
                counter += 1
                idx = current_idx
        if counter == 1:
            kids_dict[kid_type].append(name)
            kids_list.remove((idx, name))

    for _, kid_name in kids_list:
        kids_dict['Not found'].append(kid_name)

    result = ''

    for k, v in kids_dict.items():
        if v:
            result += f'{k}: {", ".join(v)}\n'

    return result.strip()


print(naughty_or_nice_list(
    [
        (3, "Amy"),
        (1, "Tom"),
        (7, "George"),
        (3, "Katy"),
    ],
    "3-Nice",
    "1-Naughty",
    Amy="Nice",
    Katy="Naughty",
))

print()

print(naughty_or_nice_list(
    [
        (7, "Peter"),
        (1, "Lilly"),
        (2, "Peter"),
        (12, "Peter"),
        (3, "Simon"),
    ],
    "3-Nice",
    "5-Naughty",
    "2-Nice",
    "1-Nice",
    ))

print()

print(naughty_or_nice_list(
    [
        (6, "John"),
        (4, "Karen"),
        (2, "Tim"),
        (1, "Merry"),
        (6, "Frank"),
    ],
    "6-Nice",
    "5-Naughty",
    "4-Nice",
    "3-Naughty",
    "2-Nice",
    "1-Naughty",
    Frank="Nice",
    Merry="Nice",
    John="Naughty",
))





