# •	На първи ред: цената в долари за процесора – реално число в интервала [200.00 … 3000.00]
# •	На втори ред: цената в долари за видео карта – реално число в интервала [100.00 … 1500.00]
# •	На трети ред: цената в долари за една RAM памет – реално число в интервала [80.00 ... 500.00]
# •	На четвърти: ред брой RAM памети – цяло число в интервала [1 ... 4]
# •   На пети ред: процент отстъпка – реално число в интервала [0.01 … 0.1]

price_processor = float(input())
price_graphic_card = float(input())
price_ram = float(input())
quantity_ram = int(input())
percentage_discount = float(input())

sum_processor = price_processor * 1.57
sum_graphic_card = price_graphic_card * 1.57
percentage_coeficient = (1 - percentage_discount)
sum_ram = price_ram * quantity_ram * 1.57

total_sum = ((sum_processor + sum_graphic_card) * percentage_coeficient) + sum_ram

print(f"Money needed - {total_sum:.2f} leva.")
