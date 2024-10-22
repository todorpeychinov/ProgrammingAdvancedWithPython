from collections import deque

seats = input().split(', ')
sequence_1 = deque(input().split(', '))
sequence_2 = deque(input().split(', '))
rotations = 0
matched_seats = []

while sequence_1 and sequence_2:

    if len(matched_seats) == 3:
        break

    if rotations == 10:
        break

    num_1 = sequence_1.popleft()
    num_2 = sequence_2.pop()

    sum = int(num_1) + int(num_2)
    ch = chr(sum)

    seat_1 = num_1 + ch
    seat_2 = num_2 + ch


    for seat in [seat_1, seat_2]:
        if seat in matched_seats:
            break
        if seat in seats:
            seats.remove(seat)
            matched_seats.append(seat)
            break
    else:
        sequence_1.append(num_1)
        sequence_2.appendleft(num_2)

    rotations += 1


print(f'Seat matches: {", ".join(matched_seats)}')
print(f"Rotations count: {rotations}")



#


