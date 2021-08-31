price_puzzle = 2.60
price_dull = 3
price_bear = 4.10
price_minion = 8.20
price_truck = 2

# 1.	Цена на екскурзията - реално число;
price_excursion = float(input())
# 2.	Брой пъзели - цяло число;
quantity_puzzle = int(input())
# 3.	Брой говорещи кукли - цяло число;
quantity_dull = int(input())
# 4.	Брой плюшени мечета - цяло число;
quantity_bear = int(input())
# 5.	Брой миньони - цяло число;
quantity_minion = int(input())
# 6.	Брой камиончета - цяло число.
quantity_truck = int(input())

total_quantity = quantity_puzzle + quantity_dull + quantity_bear + quantity_minion + quantity_truck
total_sum = (quantity_puzzle * price_puzzle + quantity_dull * price_dull + quantity_bear * price_bear + quantity_minion
             * price_minion + quantity_truck * price_truck)
sum_after_rent = total_sum * 0.9


if total_quantity >= 50:
    sum_after_rent *= 0.75


money_left = sum_after_rent - price_excursion

if sum_after_rent >= price_excursion:
    print(f"Yes! {money_left:.2f} lv left.")
else:
    print(f"Not enough money! {abs(money_left):.2f} lv needed.")
