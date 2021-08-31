input_str = input()

products_dict = {}

while input_str != "buy":

    product_price_qty = input_str.split()

    product = product_price_qty[0]
    price = float(product_price_qty[1])
    quantity = int(product_price_qty[2])

    if product in products_dict:
        if products_dict[product][0] != price:
            products_dict[product][0] = price
            products_dict[product][1] += quantity
        else:
            products_dict[product][1] += quantity
    else:
        products_dict [product] = [price, quantity]

    input_str = input()

for key, val in products_dict.items():
    print(f'{key} -> {val[0] * val[1]:.2f}')
