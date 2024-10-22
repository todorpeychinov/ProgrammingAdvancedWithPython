from collections import deque

presents = {}

presents_dict = {
    150: 'Doll',
    250: 'Wooden train',
    300: 'Teddy bear',
    400: 'Bicycle'
}

materials = list(map(int, input().split()))
magic = deque(list(map(int, input().split())))

while materials and magic:
    current_magic = materials[-1] * magic[0]
    if current_magic in presents_dict:
        current_present = presents_dict[current_magic]
        if current_present not in presents:
            presents[current_present] = 0
        presents[current_present] += 1
        materials.pop()
        magic.popleft()
    elif current_magic < 0:
        materials.append(materials.pop() + magic.popleft())
    elif current_magic > 0:
        magic.popleft()
        materials[-1] += 15
    else:
        if magic[0] == 0:
            magic.popleft()
        if materials[-1] == 0:
            materials.pop()


if ('Doll' in presents and 'Wooden train' in presents) or \
     ('Teddy bear' in presents and 'Bicycle' in presents):
    print("The presents are crafted! Merry Christmas!")
else:
    print("No presents this Christmas!")

if materials:
    print(f"Materials left: {', '.join([str(material) for material in materials[::-1]])}")
if magic:
    print(f"Magic left: {', '.join([str(magic_num) for magic_num in magic])}")

for k, v in sorted(presents.items()):
    print(f"{k}: {v}")

