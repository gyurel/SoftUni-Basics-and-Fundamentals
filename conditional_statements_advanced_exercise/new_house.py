# •	Вид цветя - текст с възможности "Roses", "Dahlias", "Tulips", "Narcissus" или "Gladiolus";
# •	Брой цветя - цяло число;
# •	Бюджет - цяло число.

type_flowers = input()
count_flowers = int(input())
budget = int(input())

total_sum = 0
# цвете	        Роза	Далия	Лале	Нарцис	Гладиола
# Цена лева	       5	3.80	2.80	 3	        2.50


# •	Ако Нели купи повече от 80 Рози - 10% отстъпка от крайната цена;
# •	Ако Нели купи повече от 90  Далии - 15% отстъпка от крайната цена;
# •	Ако Нели купи повече от 80 Лалета - 15% отстъпка от крайната цена;
# •	Ако Нели купи по-малко от 120 Нарциса - цената се оскъпява с 15%;
# •	Ако Нели Купи по-малко от 80 Гладиоли - цената се оскъпява с 20%.

if type_flowers == "Roses":
    if count_flowers > 80:
        total_sum = count_flowers * 5 * 0.9
    else:
        total_sum = count_flowers * 5

elif type_flowers == "Dahlias":
    if count_flowers > 90:
        total_sum = count_flowers * 3.8 * 0.85
    else:
        total_sum = count_flowers * 3.8

elif type_flowers == "Tulips":
    if count_flowers > 80:
        total_sum = count_flowers * 2.8 * 0.85
    else:
        total_sum = count_flowers * 2.8

elif type_flowers == "Narcissus":
    if count_flowers < 120:
        total_sum = count_flowers * 3 * 1.15
    else:
        total_sum = count_flowers * 3

elif type_flowers == "Gladiolus":
    if count_flowers < 80:
        total_sum = count_flowers * 2.5 * 1.2
    else:
        total_sum = count_flowers * 2.5


if budget >= total_sum:
    money_left = budget - total_sum
    print(f"Hey, you have a great garden with {count_flowers} {type_flowers} and {money_left:.2f} leva left.")
else:
    money_shortage = total_sum - budget
    print(f"Not enough money, you need {money_shortage:.2f} leva more.")
