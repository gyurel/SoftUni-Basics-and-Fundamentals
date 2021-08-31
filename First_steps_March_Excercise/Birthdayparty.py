#•	Торта  – цената ѝ е 20% от наема на залата
#•	Напитки – цената им е 45% по-малко от тази на тортата
#•	Аниматор – цената му е 1/3 от цената за наема на залата

rent_hall = int(input())

price_cake = rent_hall * 0.2
drinks = price_cake * 0.55
animator = rent_hall/3

expenses = rent_hall + price_cake + drinks + animator
print(expenses)
