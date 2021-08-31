# 1.	Цена на ягодите в лева – реално число;
# 2.	Количество на бананите в килограми – реално число;
# 3.	Количество на портокалите в килограми – реално число;
# 4.	Количество на малините в килограми – реално число;
# 5.	Количество на ягодите в килограми – реално число.

price_strawberries = float(input())
quantity_bananas = float(input())
quantity_oranges = float(input())
quantity_raspberries = float(input())
quantity_strawberries = float(input())

# •	цената на  малините е на половина по-ниска от тази на ягодите;
# •	цената на портокалите е с 40% по-ниска от цената на малините;
# •	цената на бананите е с 80% по-ниска от цената на малините.

price_raspberries = price_strawberries / 2
price_oranges = price_raspberries - (price_raspberries * 0.4)
price_bananas = price_raspberries - (price_raspberries * 0.8)

# Да се напише програма, която пресмята колко пари са  ѝ необходими за да плати сметката

total_sum = (price_bananas * quantity_bananas) + (price_oranges * quantity_oranges) + (price_raspberries * quantity_raspberries) + (price_strawberries * quantity_strawberries)
print(total_sum)

