gifts = input().split()

command1 = "OutOfStock"
command2 = "Required"
command3 = "JustInCase"

command_terminate = "No Money"

command = input()

while command != command_terminate:
    command_list = command.split()

    if command_list[0] == command1:
        for gift in gifts:
            if gift == command_list[1]:
                index_of_el = gifts.index(gift)
                gifts[index_of_el] = "None"

    elif command_list[0] == command2:
        for i in range(len(gifts)):
            if i == int(command_list[2]):
                gifts[i] = command_list[1]

    elif command_list[0] == command3:
        gifts[len(gifts) - 1] = command_list[1]
    command = input()

for gift in gifts:
    if gift != "None":
        print(gift, end=" ")
