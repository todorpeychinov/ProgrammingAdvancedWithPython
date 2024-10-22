from collections import deque

elfs_energy = deque(int(el) for el in input().split())
materials = [int(el) for el in input().split()]

total_energy_used = 0
toys = 0
turn = 1

while elfs_energy and materials:
    energy = elfs_energy.popleft()
    if energy < 5:
        continue

    needed_materials = materials.pop()

    if turn % 3 != 0:
        if energy >= needed_materials:
            energy -= needed_materials
            total_energy_used += needed_materials
            if turn % 5 != 0:
                toys += 1
                energy += 1
            elfs_energy.append(energy)
        else:
            materials.append(needed_materials)
            energy *= 2
            elfs_energy.append(energy)
    else:
        if energy >= (needed_materials * 2):
            energy -= (needed_materials * 2)
            total_energy_used += (needed_materials * 2)
            if turn % 5 != 0:
                toys += 2
                energy += 1
            elfs_energy.append(energy)
        else:
            materials.append(needed_materials)
            energy *= 2
            elfs_energy.append(energy)

    turn += 1


print(f"Toys: {toys}")
print(f"Energy: {total_energy_used}")

if elfs_energy:
    print(f'Elves left: {", ".join(str(el) for el in elfs_energy)}')
if materials:
    print(f'Boxes left: {", ".join(str(el) for el in materials)}')
