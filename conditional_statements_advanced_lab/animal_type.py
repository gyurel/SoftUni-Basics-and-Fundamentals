# 1.	dog -> mammal
# 2.	crocodile, tortoise, snake -> reptile
# 3.	others -> unknown

animal = input()
animal_type = ""

if animal == "dog":
    animal_type = "mammal"
elif animal == "crocodile" or animal == "tortoise" or animal == "snake":
    animal_type = "reptile"
else:
    animal_type = "unknown"
print(animal_type)
