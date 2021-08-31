aray_ints = [int(el) for el in input().split()]

commands = input()

while commands is not "end":
    if commands == "decrease":
        for el in aray_ints:
            el -= 1
    else:
        command = commands.split()
        if command[0] == "swap":
            aray_ints[int(command[2])] = aray_ints[int(command[1])]
        elif command[0] == "multiply":
            product = int(aray_ints[int(command[1])] * aray_ints[int(command[2])])
            aray_ints.pop(int(command[1]))
            aray_ints.insert(int(command[1]), product)

    commands = input()

print(*aray_ints, sep=", ")
