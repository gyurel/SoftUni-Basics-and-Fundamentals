neighbourhood = input().split("@")


mission_successfull = True
house_count = 0
current_index = 0

command = input()
while not command == "Love!":
    command = command.split()
    jump_len = int(command[1])
    current_jump_index = current_index + jump_len

    if len(neighbourhood) - 1 < current_jump_index:
        current_jump_index = 0

    current_value = int(neighbourhood[current_jump_index])

    if current_value == 0:
        print(f"Place {current_jump_index} already had Valentine's day.")
    else:
        current_value -= 2
        neighbourhood.pop(current_jump_index)
        neighbourhood.insert(current_jump_index, str(current_value))
        if current_value == 0:
            print(f"Place {current_jump_index} has Valentine's day.")

    current_index = current_jump_index
    command = input()

print(f"Cupid's last position was {current_index}.")

for el in neighbourhood:
    if not int(el) == 0:
        house_count += 1
        mission_successfull = False

if mission_successfull:
    print(f"Mission was successful.")
else:
    print(f"Cupid has failed {house_count} places.")
