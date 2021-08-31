cities = input()

command_line = input()

while not command_line == "Travel":

    command_line = command_line.split(":")
    command = command_line[0]

    if command == "Add Stop":
        index = int(command_line[1])
        new_city = command_line[2]
        if 0 <= index < len(cities):
            first_part = cities[0:index]
            last_part = cities[index:]
            cities = first_part + new_city + last_part
        print(f"{cities}")

    elif command == "Remove Stop":
        start_index = int(command_line[1])
        end_index = int(command_line[2])
        if 0 <= start_index < len(cities) and 0 <= end_index < len(cities):
            remove_slice = cities[start_index:end_index+1]
            cities = cities.replace(remove_slice, "")
        print(f"{cities}")

    elif command == "Switch":
        city_to_remove = command_line[1]
        city_to_insert = command_line[2]
        if city_to_remove in cities:
            cities = cities.replace(city_to_remove, city_to_insert)
        print(f"{cities}")

    command_line = input()

print(f"Ready for world tour! Planned stops: {cities}")
