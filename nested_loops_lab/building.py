# От конзолата се прочитат две цели числа - броят на етажите и броят на стаите за един етаж.

storeys = int(input())
number_rooms = int(input())
floor = 0

for floor in range(storeys, 0, -1):
    for rooms in range(0, number_rooms):
        if floor == storeys:
            print(f"L{floor}{rooms}", end=" ")
        elif floor % 2 == 0:
            print(f"O{floor}{rooms}", end=" ")
        else:
            print(f"A{floor}{rooms}", end=" ")
    print()
