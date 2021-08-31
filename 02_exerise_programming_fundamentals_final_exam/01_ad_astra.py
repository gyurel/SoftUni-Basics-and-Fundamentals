import re

pattern = r"([|#])(?P<name>[A-Za-z\s]+)(\1)(?P<date>[0-9]{2}/[0-9]{2}/[0-9]{2})(\1)(?P<calories>[0-9]+)(\1)"

food_name = []
exp_date = []
calories = []
total_calories = 0

input_string = input()

food_info = re.finditer(pattern, input_string)

for match in food_info:
    name = match.group('name')
    date = match.group('date')
    cal = int(match.group('calories'))
    total_calories += cal
    food_name.append(name)
    exp_date.append(date)
    calories.append(cal)

print(f"You have food to last you for: {int(total_calories / 2000)} days!")


for i in range(len(food_name)):
    print(f"Item: {food_name[i]}, Best before: {exp_date[i]}, Nutrition: {calories[i]}")
