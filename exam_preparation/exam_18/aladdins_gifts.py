from collections import deque


def check_range(result):
    if 100 <= result <= 199:
        gifts["Gemstone"] += 1
        return True

    elif 200 <= result <= 299:
        gifts["Porcelain Sculpture"] += 1
        return True

    elif 300 <= result <= 399:
        gifts["Gold"] += 1
        return True

    elif 400 <= result <= 499:
        gifts["Diamond Jewellery"] += 1
        return True


materials = [int(el) for el in input().split()]
magic_level = deque([int(el) for el in input().split()])

gifts = {
    "Gemstone": 0,
    "Porcelain Sculpture": 0,
    "Gold": 0,
    "Diamond Jewellery": 0
}

while materials and magic_level:
    material = materials.pop()
    magic = magic_level.popleft()

    sum_nums = material + magic

    if check_range(sum_nums):
        continue

    elif sum_nums < 100:
        if sum_nums % 2 == 0:
            material *= 2
            magic *= 3
            sum_nums = material + magic
            check_range(sum_nums)
        else:
            sum_nums *= 2
            check_range(sum_nums)

    elif sum_nums > 499:
        sum_nums /= 2
        check_range(sum_nums)


if (gifts["Gemstone"] > 0 and gifts["Porcelain Sculpture"] > 0) or (gifts["Gold"] > 0 and gifts["Diamond Jewellery"] > 0):
    print("The wedding presents are made!")
else:
    print("Aladdin does not have enough wedding presents.")

if materials:
    print(f'Materials left: {", ".join(str(el) for el in materials)}')
if magic_level:
    print(f'Magic left: {", ".join(str(el) for el in magic_level)}')

for gift, count in sorted(gifts.items(), key=lambda x: x[0]):
    if count > 0:
        print(f'{gift}: {count}')


