age = int(input())
price_washing_machine = float(input())
price_toy = int(input())

sum_birhtday_money = 0
birthday_money = int()
count_toy = 0
total_money = sum_birhtday_money + count_toy * price_toy


for i in range(1, age+1):
    if i % 2 == 0:
        birthday_money += 10
        sum_birhtday_money += birthday_money - 1
    else:
        count_toy += 1

total_money = sum_birhtday_money + count_toy * price_toy

# •	Ако парите на Лили са достатъчни:
# o	"Yes! {N}" - където N е остатъка пари след покупката
# •	Ако парите не са достатъчни:
# o	"No! {М}" - където M е сумата, която не достига
# •	Числата N и M трябва да за форматирани до вторият знак след десетичната запетая.

if total_money >= price_washing_machine:
    rest = total_money - price_washing_machine
    print(f"Yes! {rest:.2f}")
else:
    shortage = price_washing_machine - total_money
    print(f"No! {shortage:.2f}")
