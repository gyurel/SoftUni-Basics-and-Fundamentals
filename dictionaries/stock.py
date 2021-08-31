stocks_list = input().split()

stocks_dict = {}

for _ in range(0, len(stocks_list), 2):
    key = stocks_list[_]
    value = stocks_list[_ + 1]
    stocks_dict[key] = int(value)

products = input().split()

for product in products:
    if product in stocks_dict:
        print(f"We have {stocks_dict[product]} of {product} left")
    else:
        print(f"Sorry, we don't have {product}")
