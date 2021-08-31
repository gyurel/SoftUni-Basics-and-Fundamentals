budget = float(input())
statist = int(input())
price_cloths = float(input())
price_decor = budget * 0.1

if statist > 150:
    price_cloths *= 0.9

balans = budget - statist * price_cloths - price_decor

if balans < 0:
    print("Not enough money!")
    print(f"Wingard needs {abs(balans):.2f} leva more.")
else:
    print("Action!")
    print(f"Wingard starts filming with {balans:.2f} leva left.")