events_string = input().split("|")

energy = 100
coins = 100
bankrupt = False

for event in events_string:

    current_event = event.split("-")

    if current_event[0] == "rest":
        lack_of_energy = abs(energy - 100)
        if int(current_event[1]) > lack_of_energy:
            energy += lack_of_energy
            print(f"You gained {lack_of_energy} energy.")
        else:
            energy += int(current_event[1])
            print(f"You gained {int(current_event[1])} energy.")

        print(f"Current energy: {energy}.")

    elif current_event[0] == "order":
        if energy >= 30:
            coins += int(current_event[1])
            energy -= 30
            print(f"You earned {int(current_event[1])} coins.")
        else:
            energy += 50
            print("You had to rest!")
            continue
    else:
        if coins >= int(current_event[1]):
            coins -= int(current_event[1])
            print(f"You bought {current_event[0]}.")
            if coins <= 0:
                bankrupt = True
                print(f"Closed! Cannot afford {current_event[0]}.")
                break
        else:
            bankrupt = True
            print(f"Closed! Cannot afford {current_event[0]}.")
            break

if not bankrupt:
    print(f"Day completed!")
    print(f"Coins: {coins}")
    print(f"Energy: {energy}")
