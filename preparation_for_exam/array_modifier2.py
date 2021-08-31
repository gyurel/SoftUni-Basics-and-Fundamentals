aray_ints = [int(el) for el in input().split()]

commands = input()

while not commands == "end":

    if commands == "decrease":
        for i in range(len(aray_ints)):
            aray_ints[i] -= 1
    else:
        command = commands.split()
        if command[0] == "swap":
            aray_ints[int(command[1])], aray_ints[int(command[2])] = aray_ints[int(command[2])], aray_ints[int(command[1])]
        elif command[0] == "multiply":
            product = int(aray_ints[int(command[1])] * aray_ints[int(command[2])])
            aray_ints.pop(int(command[1]))
            aray_ints.insert(int(command[1]), product)

    commands = input()

print(*aray_ints, sep=", ")
