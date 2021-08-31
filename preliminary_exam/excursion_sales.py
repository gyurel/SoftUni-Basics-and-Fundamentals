quantity_excursions_sea = int(input())
quantity_excursions_mountain = int(input())

# море ("sea") на цена 680 лева и планина ("mountain") на цена 499 лева
sum_sea = 0
sum_mountain = 0
all_sold = False

command = input()

while command != "Stop":
    if command == "sea":
        if quantity_excursions_sea > 0:
            quantity_excursions_sea -= 1
            sum_sea += 680
        elif quantity_excursions_sea <= 0:
            pass
    elif command == "mountain":
        if quantity_excursions_mountain > 0:
            quantity_excursions_mountain -= 1
            sum_mountain += 499
        elif quantity_excursions_mountain <= 0:
            pass
    total_quantity_excursions = quantity_excursions_mountain + quantity_excursions_sea
    if total_quantity_excursions <= 0:
        all_sold = True
        break
    command = input()

if all_sold:
    print("Good job! Everything is sold.")
    print(f"Profit: {sum_sea+sum_mountain} leva.")
else:
    print(f"Profit: {sum_sea + sum_mountain} leva.")
