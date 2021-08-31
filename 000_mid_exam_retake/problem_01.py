number_of_days = int(input())
count_players = int(input())
group_energy = float(input())
water_per_day_person = float(input())
food_per_day_person = float(input())

needed_water = number_of_days * count_players * water_per_day_person
needed_food = number_of_days * count_players * food_per_day_person
has_failed = False

for i in range(1, number_of_days + 1):
    energy_loss = float(input())
    group_energy -= energy_loss

    if group_energy <= 0:
        print(f"You will run out of energy. You will be left with {needed_food:.2f} food and {needed_water:.2f} water.")
        has_failed = True
        break

    if i % 2 == 0:
        group_energy += group_energy * 0.05
        needed_water -= needed_water * 0.3

    if i % 3 == 0:
        needed_food -= needed_food / count_players
        group_energy += group_energy * 0.1


if not has_failed:
    print(f"You are ready for the quest. You will be left with - {group_energy:.2f} energy!")
