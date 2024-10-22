from collections import deque

monsters_armor = deque([int(el) for el in input().split(',')])
soldiers_strikes = [int(el) for el in input().split(',')]
killed_monsters = 0

while monsters_armor and soldiers_strikes:
    current_monster = monsters_armor.popleft()
    current_soldier = soldiers_strikes.pop()

    if current_soldier >= current_monster:
        killed_monsters += 1
        new_impact = current_soldier - current_monster
        if new_impact > 0:
            if len(soldiers_strikes) > 0:
                soldiers_strikes[-1] += new_impact
            else:
                soldiers_strikes.append(new_impact)

    else:
        current_monster -= current_soldier
        monsters_armor.append(current_monster)

if not monsters_armor:
    print("All monsters have been killed!")
if not soldiers_strikes:
    print("The soldier has been defeated.")
print(f"Total monsters killed: {killed_monsters}")