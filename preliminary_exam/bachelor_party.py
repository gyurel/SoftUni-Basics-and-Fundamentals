# 1.	Цена на моминското парти - реално число в интервала [1.00 … 10000.00]
# 2.	Брой любовни послания - цяло число в интервала [0… 1000]
# 3.	Брой восъчни рози - цяло число в интервала [0 … 1000]
# 4.	Брой ключодържатели - цяло число в интервала [0 … 1000]
# 5.	Брой карикатури - цяло число в интервала [0 … 1000]
# 6.	Брой късмети изненада - цяло число в интервала [0 … 1000]

price_party = float(input())
number_love_messages = int(input())
price_love_messages = 0.60
number_roses = int(input())
price_roses = 7.20
number_key_holders = int(input())
price_key_holders = 3.60
number_charicatures = int(input())
price_charicatures = 18.2
number_lucks = int(input())
price_lucks = 22

total_quantity = number_lucks + number_roses + number_charicatures + number_key_holders + number_love_messages
total_sum = number_love_messages * price_love_messages + number_roses * price_roses + number_key_holders * price_key_holders + number_charicatures * price_charicatures + number_lucks * price_lucks

if total_quantity >= 25:
    total_sum *= 0.65
total_sum *= 0.9

if total_sum >= price_party:
    print(f"Yes! {abs(total_sum -price_party):.2f} lv left.")
else:
    print(f"Not enough money! {abs(total_sum -price_party):.2f} lv needed.")


