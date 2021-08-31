goods_string = input().split("|")
budget = int(input())

clothes_max = 50
shoes_max = 35
accessories_max = 20.50
list_of_new_prices = []
profit = []

for good in goods_string:
    current_good = good.split("->")
    if float(current_good[1]) > budget:
        continue
    else:
        if current_good[0] == "Clothes":
            if float(current_good[1]) > clothes_max:
                continue
            else:
                budget -= float(current_good[1])
                new_price = float(current_good[1]) * 1.4
                current_profit = new_price - float(current_good[1])
                list_of_new_prices.append(new_price)
                profit.append(current_profit)

        elif current_good[0] == "Shoes":
            if float(current_good[1]) > shoes_max:
                continue
            else:
                budget -= float(current_good[1])
                new_price = float(current_good[1]) * 1.4
                current_profit = new_price - float(current_good[1])
                list_of_new_prices.append(new_price)
                profit.append(current_profit)

        elif current_good[0] == "Accessories":
            if float(current_good[1]) > accessories_max:
                continue
            else:
                budget -= float(current_good[1])
                new_price = float(current_good[1]) * 1.4
                current_profit = new_price - float(current_good[1])
                list_of_new_prices.append(new_price)
                profit.append(current_profit)

for i in range(len(list_of_new_prices)):
    if i < len(list_of_new_prices) - 1:
        print(f"{list_of_new_prices[i]:.2f}", end=" ")
    else:
        print(f"{list_of_new_prices[i]:.2f}")

print(f"Profit: {sum(profit):.2f}")

if sum(list_of_new_prices) + budget >= 150:
    print("Hello, France!")
else:
    print("Time to go.")
