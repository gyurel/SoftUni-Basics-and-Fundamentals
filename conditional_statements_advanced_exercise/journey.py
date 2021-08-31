budget = float(input())
season = input()

destination = ""
housing = ""
expenses = 0

if budget <= 100:
    destination = "Bulgaria"        # •	При 100 лв. или по-малко - някъде в България:
    if season == "summer":
        housing = "Camp"
        expenses = budget * 0.3     # o	Лято - 30% от бюджета;
    elif season == "winter":
        housing = "Hotel"
        expenses = budget * 0.7     # o	Зима - 70% от бюджета.
elif budget <= 1000:                # •	При 1000 лв. или по малко - някъде на Балканите:
    destination = "Balkans"
    if season == "summer":
        housing = "Camp"
        expenses = budget * 0.4     # o	Лято - 40% от бюджета;
    elif season == "winter":
        housing = "Hotel"
        expenses = budget * 0.8     # o	Зима - 80% от бюджета.
elif budget > 1000:               # •	При повече от 1000 лв. - някъде из Европа:
    destination = "Europe"
    housing = "Hotel"
    expenses = budget * 0.9     # o	При пътуване из Европа, независимо от сезона, ще похарчи 90% от бюджета.

print(f"Somewhere in {destination}")
print(f"{housing} - {expenses:.2f}")
