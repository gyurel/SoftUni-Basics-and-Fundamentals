n = int(input())

plant_rarity_rating_dict = {}

for i in range(n):

    plant_rarity_info = input().split("<->")

    plant_name = plant_rarity_info[0]
    plant_raryti = int(plant_rarity_info[1])

    if plant_name not in plant_rarity_rating_dict:
        plant_rarity_rating_dict[plant_name] = {'Plant_rarity': plant_raryti, 'Ratings': []}
    else:
        plant_rarity_rating_dict[plant_name]['Plant_rarity'] = plant_raryti

command = input()

while command != "Exhibition":

    command = command.split(": ")
    to_do = command[0]
    rest = command[1]

    if to_do == "Rate":
        rest = rest.split(" - ")
        plant_name = rest[0]
        rating = int(rest[1])
        if plant_name not in plant_rarity_rating_dict:
            print("error")
        else:
            plant_rarity_rating_dict[plant_name]['Ratings'].append(rating)

    elif to_do == "Update":
        rest = rest.split(" - ")
        plant_name = rest[0]
        rarity = int(rest[1])
        if plant_name not in plant_rarity_rating_dict:
            print("error")
        else:
            plant_rarity_rating_dict[plant_name]['Plant_rarity'] = rarity

    elif to_do == "Reset":
        plant_name = rest
        if plant_name not in plant_rarity_rating_dict:
            print("error")
        else:
            plant_rarity_rating_dict[plant_name]['Ratings'] = []

    else:
        print("error")

    command = input()

for key, val in plant_rarity_rating_dict.items():
    for kvp1, val1 in val.items():
        if kvp1 == "Ratings":
            if len(val1) == 0:
                val1 = 0
                plant_rarity_rating_dict[key][kvp1] = val1
            else:
                mean_raiting = sum(val1) / len(val1)
                plant_rarity_rating_dict[key][kvp1] = mean_raiting


plant_rarity_rating_dict = {name: values for name, values in sorted(plant_rarity_rating_dict.items(), key=lambda x: (-x[1]['Plant_rarity'], -x[1]['Ratings']))}

print("Plants for the exhibition:")

for key, val in plant_rarity_rating_dict.items():
    print(f"- {key}; Rarity: {plant_rarity_rating_dict[key]['Plant_rarity']}; Rating: {plant_rarity_rating_dict[key]['Ratings']:.2f}")
