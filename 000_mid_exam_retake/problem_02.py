coffee_list = input().split()

n = int(input())

for i in range(n):
    cmd = input()

    if "Include" in cmd:
        command = cmd.split()
        coffee_name = command[1]
        coffee_list.append(coffee_name)

    elif "Remove" in cmd:
        command = cmd.split()
        to_do = command[1]
        number_of_coffees = int(command[2])

        if len(coffee_list) < number_of_coffees:
            continue

        if to_do == "first":
            first_part = coffee_list[0:number_of_coffees]
            last_part = coffee_list[number_of_coffees:]
            coffee_list = last_part

        elif to_do == "last":
            first_part = coffee_list[0:-number_of_coffees]
            last_part = coffee_list[-number_of_coffees:]
            coffee_list = first_part

    elif "Prefer" in cmd:
        command = cmd.split()
        index_1 = int(command[1])
        index_2 = int(command[2])

        if 0 <= index_1 <= len(coffee_list) - 1 and 0 <= index_2 <= len(coffee_list) - 1:
            first_coffee = coffee_list[index_1]
            second_coffee = coffee_list[index_2]

            coffee_list.pop(index_1)
            coffee_list.insert(index_1, second_coffee)
            coffee_list.pop(index_2)
            coffee_list.insert(index_2, first_coffee)

    elif "Reverse" in cmd:
        coffee_list = coffee_list[::-1]

print("Coffees:")
print(*coffee_list, sep=" ")
