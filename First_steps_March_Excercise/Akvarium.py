# От конзолата се четат 4 реда:
# 1.	Дължина в см – цяло число
# 2.	Широчина в см – цяло число
# 3.	Височина в см – цяло число
# 4.	Процент зает обем – реално число

length = int(input())
width = int(input())
height = int(input())
occuqied_percentage = float(input()) / 100

volume_in_litters = length * width * height/1000

# Да се напише програма, която изчислява литрите вода, които са необходими за напълването на аквариума.

needed_water = volume_in_litters - (volume_in_litters * occuqied_percentage)

print(needed_water)
