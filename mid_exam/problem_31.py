price_ratings_list = [int(el) for el in input().split(", ")]
entry_point = int(input())
type_of_items = input()
positon = ""

list_left_part = price_ratings_list[:entry_point]
list_right_part = price_ratings_list[entry_point + 1:]

left_element = price_ratings_list[entry_point - 1]
right_element = price_ratings_list[entry_point + 1]

if sum(list_left_part) > sum(list_right_part):
    if type_of_items == "expensive":
        positon = "Left"
        print(f"{positon} - {sum(list_left_part)}")
    elif type_of_items == "cheap":
        positon = "Right"
        print(f"{positon} - {sum(list_right_part)}")
elif sum(list_left_part) < sum(list_right_part):
    if type_of_items == "expensive":
        positon = "Right"
        print(f"{positon} - {sum(list_left_part)}")
    elif type_of_items == "cheap":
        positon = "Left"
        print(f"{positon} - {sum(list_right_part)}")
elif sum(list_left_part) == sum(list_right_part):
    if type_of_items == "expensive":
        positon = "Left"
        print(f"{positon} - {sum(list_left_part)}")
    elif type_of_items == "cheap":
        positon = "Left"
        print(f"{positon} - {sum(list_left_part)}")
