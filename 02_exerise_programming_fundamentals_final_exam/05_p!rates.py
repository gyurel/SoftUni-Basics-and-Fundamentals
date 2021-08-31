command = input()

city_dict = {}

while command != "Sail":

    city = command.split("||")
    city_name = city[0]
    population = int(city[1])
    gold = int(city[2])

    if city_name not in city_dict:
        city_dict[city_name] = {'Population': population, 'Gold': gold}
    else:
        city_dict[city_name]['Population'] += population
        city_dict[city_name]['Gold'] += gold

    command = input()


event_info = input()

while event_info != "End":

    event = event_info.split("=>")

    if "Plunder" in event:
        city_name = event[1]
        people = int(event[2])
        gold = int(event[3])

        city_dict[city_name]['Population'] -= people
        city_dict[city_name]['Gold'] -= gold
        print(f"{city_name} plundered! {gold} gold stolen, {people} citizens killed.")

        if city_dict[city_name]['Population'] == 0 or city_dict[city_name]['Gold'] == 0:
            print(f"{city_name} has been wiped off the map!")
            del city_dict[city_name]

    elif "Prosper" in event:
        city_name = event[1]
        gold = int(event[2])

        if gold < 0:
            print(f"Gold added cannot be a negative number!")
            event_info = input()
            continue

        city_dict[city_name]['Gold'] += gold
        print(f"{gold} gold added to the city treasury. {city_name} now has { city_dict[city_name]['Gold']} gold.")

    event_info = input()

city_dict_sorted = sorted(city_dict.items(), key=lambda x: (-x[1]['Gold'], x[0]))

if len(city_dict_sorted) > 0:
    print(f"Ahoy, Captain! There are {len(city_dict_sorted)} wealthy settlements to go to:")
    for key, val in city_dict_sorted:
        print(f"{key} -> Population: {val['Population']} citizens, Gold: {val['Gold']} kg")
else:
    print(f"Ahoy, Captain! All targets have been plundered and destroyed!")
