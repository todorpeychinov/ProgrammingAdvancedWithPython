from collections import deque

textiles = deque(int(el) for el in input().split())
medicals = [int(el) for el in input().split()]

items = {
    30: 'Patch',
    40: 'Bandage',
    100: 'MedKit'
}

created_items = {
    'Patch': 0,
    'Bandage': 0,
    'MedKit': 0
}

while True:
    if not medicals and not textiles:
        print("Textiles and medicaments are both empty.")
        break
    elif not textiles:
        print("Textiles are empty.")
        break
    elif not medicals:
        print("Medicaments are empty.")
        break

    textile = textiles.popleft()
    medical = medicals.pop()

    result = textile + medical

    if result in items:
        created_item = items[result]
        created_items[created_item] += 1
        continue

    elif result > 100:
        created_items['MedKit'] += 1
        remaining_resource = result - 100
        medicals[-1] += remaining_resource

    else:
        medical += 10
        medicals.append(medical)

sorted_items = sorted(created_items.items(), key=lambda x: (-x[1], x[0]))

for item, count in sorted_items:
    if count == 0:
        continue
    print(f"{item} - {count}")

if medicals:
    medicals.reverse()
    print(f'Medicaments left: {", ".join(str(el) for el in medicals)}')
if textiles:
    print(f'Textiles left: {", ".join(str(el) for el in textiles)}')


