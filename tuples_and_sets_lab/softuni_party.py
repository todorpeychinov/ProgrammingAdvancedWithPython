number_of_guests = int(input())
guests = set()

for _ in range(number_of_guests):
    guest_code = input()
    guests.add(guest_code)

command = input()

while command != "END":
    if command in guests:
        guests.remove(command)
    command = input()


print(len(guests))
for guest in sorted(guests):
    print(guest)