# paintigs_list = list(map(int, input().split()))
paintings_list = input().split()

cmd = input()

while cmd != "END":

    if "Change" in cmd:
        command = cmd.split()
        searched_number = command[1]
        switch_number = command[2]

        if searched_number in paintings_list:
            index = paintings_list.index(searched_number)
            paintings_list.pop(index)
            paintings_list.insert(index, switch_number)

    elif "Hide" in cmd:
        command = cmd.split()
        value = command[1]
        if value in paintings_list:
            paintings_list.remove(value)

    elif "Switch" in cmd:
        command = cmd.split()
        first_number = command[1]
        second_number = command[2]
        if first_number in paintings_list and second_number in paintings_list:
            first_index = paintings_list.index(first_number)
            second_index = paintings_list.index(second_number)
            paintings_list.pop(first_index)
            paintings_list.insert(first_index, second_number)
            paintings_list.pop(second_index)
            paintings_list.insert(second_index, first_number)

    elif "Insert" in cmd:
        command = cmd.split()
        index = int(command[1]) + 1
        painting_number = command[2]
        if 0 <= index <= len(paintings_list) - 1:
            paintings_list.insert(index, painting_number)

    elif "Reverse" in cmd:
        paintings_list = paintings_list[::-1]

    cmd = input()

print(' '.join(paintings_list))
