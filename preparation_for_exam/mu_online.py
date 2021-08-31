def potion(initial_health, health):
    current_health = initial_health
    initial_health += health
    if initial_health > 100:
        initial_health = 100
        healed = 100 - current_health
        print(f"You healed for {healed} hp.\nCurrent health: {initial_health} hp.")
        return initial_health
    else:
        print(f"You healed for {health} hp.\nCurrent health: {initial_health} hp.")
        return initial_health

def chest(bitcoins, found_bitcoins):
    bitcoins += found_bitcoins

    print(f"You found {found_bitcoins} bitcoins.")
    return bitcoins

def other_cases(initial_health, monster, attack, room_counter):
    initial_health -= attack
    if initial_health > 0:
        print(f"You slayed {monster}.")
        return initial_health
    else:
        print(f"You died! Killed by {monster}.")
        print(f"Best room: {room_counter}")
        return initial_health


command_string = input().split("|")

initial_health = 100
bitcoins = 0
room_counter = 0


for el in command_string:
    command = el.split()
    room_counter += 1
    if command[0] == "potion":
        initial_health = potion(initial_health, int(command[1]))
    elif command[0] == "chest":
        bitcoins = chest(bitcoins, int(command[1]))

    else:
        initial_health = other_cases(initial_health, command[0], int(command[1]), room_counter)
        if initial_health < 1:
            break


if room_counter == len(command_string):
    print(f"You've made it!\nBitcoins: {bitcoins}\nHealth: {initial_health}")
