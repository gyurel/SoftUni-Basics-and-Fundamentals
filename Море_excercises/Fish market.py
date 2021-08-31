
#•	Първи ред – цена на скумрията на килограм. Реално число в интервала [0.00…40.00]
#•	Втори ред – цена на цацата на килограм. Реално число в интервала [0.00…30.00]
#•	Трети ред – килограма паламуд. Реално число в интервала [0.00…50.00]
#•	Четвърти ред – килограма сафрид. Реално число в интервала [0.00… 70.00]
#•	Пети ред – килограма миди. Цяло число в интервала [0 ... 100]

price_skumria = float(input())
price_caca = float(input())
quantity_palamud = float(input())
quantity_safrid = float(input())
quantity_midi = int(input())

#•	Паламуд – 60% по-скъп от скумрията
#•	Сафрид – 80% по-скъп от цацата
#•	Миди – 7.50 лв. за килограм

price_palamud = price_skumria * 1.6
price_safrid = price_caca * 1.8
price_midi = 7.5

total_sum = (price_palamud * quantity_palamud) + (price_safrid * quantity_safrid) + (price_midi * quantity_midi)
print(f"{total_sum:.2f}")