#1.	Брой страници в текущата книга – цяло число;
#2.	Страници, които може да прочита за 1 час – цяло число;
#3.	Броя на дните, за които трябва да прочете книгата – цяло число;

pages = int(input())
pages_per_hpour = int(input())
days_to_read = int(input())

hours_a_day_to_read = (pages / days_to_read)/pages_per_hpour

print(hours_a_day_to_read)
