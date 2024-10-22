def accommodate(*args, **kwargs):
    available_rooms = sorted(kwargs.items(), key=lambda x: (x[1], x[0]))
    unaccommodating_people = 0
    accommodated_rooms = {}
    for index, group in enumerate(args):
        for room_name, capacity in available_rooms:
            if capacity >= group:
                available_rooms.remove((room_name, capacity))
                _, room_num = room_name.split('_')
                room_num = int(room_num)
                accommodated_rooms[room_num] = group
                break
        else:
            unaccommodating_people += group

    result = ""

    if accommodated_rooms:
        sorted_rooms = sorted(accommodated_rooms.items(), key=lambda x: x[0])
        result += f"A total of {len(accommodated_rooms)} accommodations were completed!\n"
        result += "\n".join([f"<Room {room_number} accommodates {guests_number} guests>" for room_number, guests_number in sorted_rooms])
    else:
        result += "No accommodations were completed!"

    if unaccommodating_people > 0:
        result += f"\nGuests with no accommodation: {unaccommodating_people}"

    if available_rooms:
        result += f"\nEmpty rooms: {len(available_rooms)}"

    return result


print(accommodate(5, 4, 2, room_305=6, room_410=5, room_204=2))
print()
print(accommodate(10, 9, 8, room_307=6, room_802=5))
print()
print(accommodate(1, 2, 4, 8, room_102=3, room_101=1, room_103=2))