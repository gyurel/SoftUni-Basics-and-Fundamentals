fires_str = input().split("#")
water = int(input())

# Type of Fire	Range
# High	81 - 125
# Medium	51 - 80
# Low	1 - 50

total_fire = []

for cell in fires_str:
    index = fires_str.index(cell)
    current_cell_list = cell.split(" = ")
    if current_cell_list[0] == "High":
        if not 81 <= int(current_cell_list[1]) <= 125:
            continue
        else:
            if int(current_cell_list[1]) <= water:
                water -= int(current_cell_list[1])
                total_fire.append(int(current_cell_list[1]))

    elif current_cell_list[0] == "Medium":
        if not 51 <= int(current_cell_list[1]) <= 80:
            continue
        else:
            if int(current_cell_list[1]) <= water:
                water -= int(current_cell_list[1])
                total_fire.append(int(current_cell_list[1]))

    elif current_cell_list[0] == "Low":
        if not 1 <= int(current_cell_list[1]) <= 50:
            continue
        else:
            if int(current_cell_list[1]) <= water:
                water -= int(current_cell_list[1])
                total_fire.append(int(current_cell_list[1]))

    if water <= 0:
        break

total_effort = sum(total_fire) * 0.25


print("Cells:")
for cell in total_fire:
    print(f" - {cell}")
print(f"Effort: {total_effort:.2f}")
print(f"Total Fire: {sum(total_fire)}")
