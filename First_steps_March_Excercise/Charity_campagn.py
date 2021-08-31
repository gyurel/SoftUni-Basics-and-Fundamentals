#1.	Броят на дните, в които тече кампанията – цяло число;
#2.	Броят на сладкарите – цяло число;
#3.	Броят на тортите – цяло число;
#4.	Броят на гофретите – цяло число;
#5.	Броят на палачинките – цяло число.

days = int(input())
cook = int(input())
cakes_per_day_per_cook = int(input())
wafles_per_day_per_cook = int(input())
pancakes_per_day_per_cook = int(input())

#•	Торта - 45 лв.
#•	Гофрета - 5.80 лв.
#•	Палачинка – 3.20 лв.

sum_per_day_per_cook = (cakes_per_day_per_cook * 45) + (wafles_per_day_per_cook * 5.80) + (pancakes_per_day_per_cook * 3.20)
for_all_cooks = sum_per_day_per_cook * cook
for_all_campagne = for_all_cooks * days

reised_sum = for_all_campagne - (for_all_campagne/8)

print(reised_sum)
