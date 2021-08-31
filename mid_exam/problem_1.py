quantity_food_kg = float(input()) * 1000
quantity_hay_kg = float(input()) * 1000
quantitiy_cover_kg = float(input()) * 1000
pigs_weight_kg = float(input()) * 1000


excess_food = 0
excess_hay = 0
excess_cover = 0

if_break = False


for i in range(1, 31):
    quantity_food_kg -= 300
    if i % 2 == 0:
        quantity_hay_kg -= quantity_food_kg * 0.05
    if i % 3 == 0:
        quantitiy_cover_kg -= pigs_weight_kg / 3

    if quantity_food_kg <= 0 or quantity_hay_kg <= 0 or quantitiy_cover_kg <= 0:
        if_break = True
        break

if if_break:
    print(f"Merry must go to the pet store!")
else:
    excess_food = quantity_food_kg / 1000
    excess_hay = quantity_hay_kg / 1000
    excess_cover = quantitiy_cover_kg / 1000
    print(f"Everything is fine! Puppy is happy! Food: {excess_food:.2f}, Hay: {excess_hay:.2f}, Cover: {excess_cover:.2f}.")
