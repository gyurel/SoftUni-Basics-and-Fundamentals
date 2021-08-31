n = int(input())

liters_in_tank = 0

for _ in range(n):
    current_liters = int(input())
    if liters_in_tank + current_liters <= 255:
        liters_in_tank += current_liters
    else:
        print("Insufficient capacity!")
        continue

print(liters_in_tank)
