import re

furniture_list = []
total_price = 0

pattern = r"^>>(?P<furniture_name>[A-Za-z]+)<<(?P<price>[0-9]+\.?[0-9]*)!(?P<quantity>[0-9]+)$"
# pattern = r"^>>(?P<furniture_name>[A-Za-z]+)<<(?P<price>\d+\.?\d*)!(?P<quantity>\d+)$"

input_string = input()

while input_string != "Purchase":

    current_purchase = re.match(pattern, input_string)

    if current_purchase is not None:

        current_furniture = current_purchase.group('furniture_name')
        current_prise = float(current_purchase.group('price'))
        current_quantity = int(current_purchase.group('quantity'))

        furniture_list.append(current_furniture)
        total_price += current_prise * current_quantity

    input_string = input()

print(f"Bought furniture:")

for el in furniture_list:
    print(el)

print(f"Total money spend: {total_price:.2f}")
