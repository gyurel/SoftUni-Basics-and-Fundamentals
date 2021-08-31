# 	"room for one person" – 18.00 лв за нощувка
# 	"apartment" – 25.00 лв за нощувка
# 	"president apartment" – 35.00 лв за нощувка

price_rop = 18.00
price_apartment = 25.00
price_pa = 35.00

# •	Първи ред - дни за престой - цяло число;
# •	Втори ред - вид помещение - "room for one person", "apartment" или "president apartment";

total_days = int(input())
room_type = input()
evaluation = input()
total_nights = total_days - 1
price = 0
discount_rate = 0
total_sum = 0

# вид помещение	            по-малко от 10 дни	        между 10 и 15 дни	        повече от 15 дни
# room for one person	    не ползва намаление	        не ползва намаление	        не ползва намаление
# apartment	                30% от крайната цена	    35% от крайната цена	    50% от крайната цена
# president apartment	    10% от крайната цена	    15% от крайната цена	    20% от крайната цена

if total_nights < 10:
    if room_type == "room for one person":
        discount_rate = 1
    elif room_type == "apartment":
        discount_rate = 0.7
    elif room_type == "president apartment":
        discount_rate = 0.9
elif 10 <= total_nights <= 15:
    if room_type == "room for one person":
        discount_rate = 1
    elif room_type == "apartment":
        discount_rate = 0.65
    elif room_type == "president apartment":
        discount_rate = 0.85
elif total_nights > 15:
    if room_type == "room for one person":
        discount_rate = 1
    elif room_type == "apartment":
        discount_rate = 0.5
    elif room_type == "president apartment":
        discount_rate = 0.8

if room_type == "room for one person":
    price = price_rop
elif room_type == "apartment":
    price = price_apartment
elif room_type == "president apartment":
    price = price_pa

total_sum = total_nights * price * discount_rate

if evaluation == "positive":
    total_sum *= 1.25
elif evaluation == "negative":
    total_sum *= 0.9

print(f"{total_sum:.2f}")
