#•	Първи ред – Цена за килограм зеленчуци – реално число[0.00… 1000.00]
#•	Втори ред – Цена за килограм плодове – реално число[0.00… 1000.00]
#•	Трети ред – Общо килограми на зеленчуците – цяло число[0… 1000]
#•	Четвърти ред – Общо килограми на плодовете – цяло число[0… 1000]

price_veg = float(input())
price_fruits = float(input())
quantity_veg = int(input())
quantity_fruits = int(input())

sum_veg = price_veg * quantity_veg
sum_fruits = price_fruits * quantity_fruits
total_sum = sum_veg + sum_fruits
eur_sum = total_sum / 1.94

print(f"{eur_sum:.2f}")
