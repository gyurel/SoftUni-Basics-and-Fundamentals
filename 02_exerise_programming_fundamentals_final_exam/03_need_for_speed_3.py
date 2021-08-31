n = int(input())

cars_dict = {}

for i in range(n):
    cars = input().split("|")
    car_name = cars[0]
    mileage = int(cars[1])
    fuel = int(cars[2])
    cars_dict[car_name] = {'Mileage': mileage, 'Fuel': fuel}

command = input()

while command != "Stop":

    if "Drive" in command:
        cmd = command.split(" : ")
        car_name = cmd[1]
        distance = int(cmd[2])
        needed_fuel = int(cmd[3])
        if needed_fuel > cars_dict[car_name]['Fuel']:
            print("Not enough fuel to make that ride")
        else:
            cars_dict[car_name]['Mileage'] += distance
            cars_dict[car_name]['Fuel'] -= needed_fuel
            print(f"{car_name} driven for {distance} kilometers. {needed_fuel} liters of fuel consumed.")

        if cars_dict[car_name]['Mileage'] >= 100_000:
            del cars_dict[car_name]
            print(f"Time to sell the {car_name}!")

    elif "Refuel" in command:
        cmd = command.split(" : ")
        car_name = cmd[1]
        fuel = int(cmd[2])
        free_space = 75 - cars_dict[car_name]['Fuel']
        if fuel > free_space:
            cars_dict[car_name]['Fuel'] += free_space
            print(f"{car_name} refueled with {free_space} liters")
        else:
            cars_dict[car_name]['Fuel'] += fuel
            print(f"{car_name} refueled with {fuel} liters")

    elif "Revert" in command:
        cmd = command.split(" : ")
        car_name = cmd[1]
        kilometers = int(cmd[2])
        cars_dict[car_name]['Mileage'] -= kilometers
        if cars_dict[car_name]['Mileage'] < 10_000:
            cars_dict[car_name]['Mileage'] = 10_000
        else:
            print(f"{car_name} mileage decreased by {kilometers} kilometers")

    command = input()

# cars_dict_sorted = sorted(cars_dict.items(), key=lambda x: (-x[1]['Mileage'], x[0]))

for key, val in sorted(cars_dict.items(), key=lambda x: (-x[1]['Mileage'], x[0])):
    print(f"{key} -> Mileage: {val['Mileage']} kms, Fuel in the tank: {val['Fuel']} lt.")
