initial_energy = int(input())


distance = input()
won_battles_count = 0

while distance != "End of battle":
    if initial_energy < int(distance):
        print(f"Not enough energy! Game ends with {won_battles_count} won battles and {initial_energy} energy")
        break

    initial_energy -= int(distance)
    won_battles_count += 1

    if won_battles_count % 3 == 0:
        initial_energy += won_battles_count

    distance = input()


if distance == "End of battle":
    print(f"Won battles: {won_battles_count}. Energy left: {initial_energy}")
