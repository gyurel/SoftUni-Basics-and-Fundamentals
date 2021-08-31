# •	Бюджет на групата - цяло число;
# •	Сезон -  текст: "Spring", "Summer", "Autumn" или "Winter";
# •	Брой рибари - цяло число.

budget = int(input())
season = input()
count_fishers = int(input())

rent_boat = 0

if season == "Spring":
    rent_boat = 3000
elif season == "Summer" or season == "Autumn":
    rent_boat = 4200
elif season == "Winter":
    rent_boat = 2600

if count_fishers <= 6:
    rent_boat *= 0.9
elif 7 <= count_fishers <= 11:
    rent_boat *= 0.85
elif 12 <= count_fishers:
    rent_boat *= 0.75

if count_fishers % 2 == 0 and season != "Autumn":
    rent_boat *= 0.95

if budget >= rent_boat:
    money_left = budget - rent_boat
    print(f"Yes! You have {money_left:.2f} leva left.")
else:
    money_shortage = rent_boat - budget
    print(f"Not enough money! You need {money_shortage:.2f} leva.")
