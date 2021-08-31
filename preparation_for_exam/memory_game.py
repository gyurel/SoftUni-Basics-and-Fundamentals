elements = [el for el in input().split()]

current_number_of_moves = 0


command = input()
while True:

    current_number_of_moves += 1

    if command == "end":
        print(f"Sorry you lose :(\n{' '.join(elements)}")
        break

    command_splited = [int(el) for el in command.split()]

    if command_splited[0] == command_splited[1] or command_splited[0] < 0 or len(elements) -1 < command_splited[0] or command_splited[1] < 0 or len(elements) -1 < command_splited[1]:
        part_one = elements[:int(len(elements) / 2)]
        part_two = elements[int(len(elements) / 2) :]
        append_list = [(f"-{current_number_of_moves}a")] * 2
        elements = part_one + append_list + part_two
        print(f"Invalid input! Adding additional elements to the board")
        command = input()
        continue

    if elements[command_splited[0]] == elements[command_splited[1]]:
        print_element = elements[command_splited[0]]
        elements = [el for el in elements if el != print_element]
        print(f"Congrats! You have found matching elements - {print_element}!")

    elif not elements[command_splited[0]] == elements[command_splited[1]]:
        print(f"Try again!")


    if len(elements) == 0:
        print(f"You have won in {current_number_of_moves} turns!")
        break

    command = input()
