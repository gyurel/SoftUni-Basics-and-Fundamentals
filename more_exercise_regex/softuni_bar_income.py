import re

pattern = r"^%(?P<customer>[A-Z][a-z]+)%[^|\$%\.]*<(?P<product>\w+)>[^|\$%\.]*\|(?P<count>\d+)\|[^|\$%\.]*?(?P<price>\d+\.?\d*)\$$"
total_income = []

command = input()

while command != "end of shift":

    sells = re.match(pattern, command)
    if sells != None:

        customer = sells.group('customer')
        product = sells.group('product')
        count = int(sells.group('count'))
        price = float(sells.group('price'))
        total = price * count
        total_income.append(total)

        print(f"{customer}: {product} - {total:.2f}")

    command = input()

print(f"Total income: {sum(total_income):.2f}")
