price_ratings_list = [int(el) for el in input().split(", ")]
entry_point = int(input())
type_of_items = input()
positon = ""

list_left_part = price_ratings_list[:entry_point]
list_right_part = price_ratings_list[entry_point + 1:]
sum_list_left = []
sum_list_right = []


for el in list_left_part:
    if type_of_items == "expensive":
        if el >= price_ratings_list[entry_point]:
            sum_list_left.append(el)
    elif type_of_items == "cheap":
        if el < price_ratings_list[entry_point]:
            sum_list_left.append(el)

for el in list_right_part:
    if type_of_items == "expensive":
        if el >= price_ratings_list[entry_point]:
            sum_list_right.append(el)
    elif type_of_items == "cheap":
        if el < price_ratings_list[entry_point]:
            sum_list_right.append(el)

if sum(sum_list_left) >= sum(sum_list_right):
    positon = "Left"
    print(f"{positon} - {sum(sum_list_left)}")
elif sum(sum_list_left) < sum(sum_list_right):
    positon = "Right"
    print(f"{positon} - {sum(sum_list_right)}")
