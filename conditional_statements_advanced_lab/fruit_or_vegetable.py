# •	Плодовете "fruit" имат следните възможни стойности:  banana, apple, kiwi, cherry, lemon и grapes;
# •	Зеленчуците "vegetable" имат следните възможни стойности:  tomato, cucumber, pepper и carrot;
# •	Всички останали са "unknown".


plant = input()
plant_type = ""

if plant == "banana" or plant == "apple" or plant == "kiwi" or plant == "cherry" or plant == "lemon" or plant == "grapes":
    plant_type = "fruit"
elif plant == "tomato" or plant == "cucumber" or plant == "pepper" or plant == "carrot":
    plant_type = "vegetable"
else:
    plant_type = "unknown"
print(plant_type)
