pirate_ship = [int(el) for el in input().split(">")]
warship = [int(el) for el in input().split(">")]
max_health_of_a_section = int(input())


commands = input()

while not commands == "Retire":

    if commands == "Status":
        need_repair_count = 0
        for el in pirate_ship:
            if el < max_health_of_a_section * 0.2:
                need_repair_count += 1
        print(f"{need_repair_count} sections need repair.")

    else:

        command = commands.split()
        if command[0] == "Fire":
            index = int(command[1])
            damage = int(command[2])
            if 0 <= index <= len(warship) - 1:
                warship[index] -= damage
                if warship[index] <= 0:
                    print("You won! The enemy ship has sunken.")
                    exit(0)

            else:
                commands = input()
                continue

        elif command[0] == "Defend":
            start_index = int(command[1])
            end_index = int(command[2])
            damage = int(command[3])
            if 0 <= start_index <= len(pirate_ship)  - 1 and 0 <= end_index <= len(pirate_ship) - 1:
                for i in range(start_index, end_index + 1):
                    pirate_ship[i] -= damage
                    if pirate_ship[i] <= 0:
                        print("You lost! The pirate ship has sunken.")
                        exit(0)


            else:
                commands = input()
                continue

        elif command[0] == "Repair":
            index = int(command[1])
            health = int(command[2])
            if 0 <= index <= len(pirate_ship) - 1:
                pirate_ship[index] += health
                if pirate_ship[index] > max_health_of_a_section:
                    pirate_ship[index] = max_health_of_a_section

            else:
                commands = input()
                continue

    commands = input()


print(f"Pirate ship status: {sum(pirate_ship)}")
print(f"Warship status: {sum(warship)}")
