friends_list = input().split(", ")

command = input()

while True:
    if command != "Report":
        current_command = command.split()

        if current_command[0] == "Blacklist":
            if current_command[1] in friends_list:
                current_index = friends_list.index(current_command[1])
                current_name = friends_list[current_index]

                friends_list.pop(current_index)
                friends_list.insert(current_index, "Blacklisted")
                print(f"{current_name} was blacklisted.")
            else:
                print(f"{current_command[1]} was not found.")
                command = input()
                continue

        elif current_command[0] == "Error":
            index = int(current_command[1])
            current_name = friends_list[index]
            if 0 <= index < len(friends_list) and friends_list[index] != "Blacklisted" and friends_list[index] != "Lost":
                friends_list.pop(index)
                friends_list.insert(index, "Lost")
                print(f"{current_name} was lost due to an error.")
            else:
                command = input()
                continue
        elif current_command[0] == "Change":
            index = int(current_command[1])
            if 0 <= index < len(friends_list):
                current_name = friends_list[index]
                new_name = current_command[2]
                friends_list.pop(index)
                friends_list.insert(index, new_name)
                print(f"{current_name} changed his username to {new_name}.")
            else:
                command = input()
                continue

        command = input()
    else:
        blacklisted_names_count = 0
        lost_names_count = 0

        for el in friends_list:
            if el == "Blacklisted":
                blacklisted_names_count += 1
            if el == "Lost":
                lost_names_count += 1

        print(f"Blacklisted names: {blacklisted_names_count} ")
        print(f"Lost names: {lost_names_count}")
        print(" ".join(friends_list))
        break
