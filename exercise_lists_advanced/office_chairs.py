def chairs_check(num_rooms):

    room_number = 0
    chair_shortage_list = []
    chair_shortage = 0
    extra_chairs = 0
    result = []
    for room in range(1, num_rooms + 1):
        room_number += 1
        room_data = input().split()
        revision = len(room_data[0]) - int(room_data[1])
        if revision < 0:
            chair_shortage_list.append(f"{abs(revision)} more chairs needed in room {room_number}")
            chair_shortage += abs(revision)
        else:
            extra_chairs += abs(revision)

    if extra_chairs >= chair_shortage:
        result.append(f"Game On, {extra_chairs} free chairs left")
    else:
        result = chair_shortage_list

    return result

num_rooms = int(input())

for el in chairs_check(num_rooms):
    print(el)
