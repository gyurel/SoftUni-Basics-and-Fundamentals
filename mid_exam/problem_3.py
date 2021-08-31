price_ratings_list = [int(el) for el in input().split(", ")]
entry_point = int(input())
type_of_items = input()
positon = ""

list_left_part = price_ratings_list[:entry_point]
list_right_part = price_ratings_list[entry_point + 1:]

left_element = price_ratings_list[entry_point - 1]
right_element = price_ratings_list[entry_point + 1]
if type_of_items == "expensive":
    if left_element > right_element:
        positon = "Left"
    elif left_element < right_element:
        positon = "Right"
    elif left_element == right_element:
        positon = "Left"

    if positon == "Left":
        print(f"{positon} - {sum(list_left_part)}")
    elif positon == "Right":
        print(f"{positon} - {sum(list_right_part)}")
else:
    if left_element < right_element:
        positon = "Left"
    elif left_element > right_element:
        positon = "Right"
    elif left_element == right_element:
        positon = "Left"

    if positon == "Left":
        print(f"{positon} - {sum(list_left_part)}")
    elif positon == "Right":
        print(f"{positon} - {sum(list_right_part)}")
