integers_list = [int(el) for el in input().split()]

average_value = 0
sum_ints = 0
top_five = []

for el in integers_list:
    sum_ints += el

average_value = sum_ints / len(integers_list)

for i in range(5):
    current_element = max(integers_list)
    if current_element > average_value:
        top_five.append(current_element)
        integers_list.remove(current_element)

top_five.sort(reverse= True)

if len(top_five) == 0:
    print("No")
else:
    print(*top_five, sep=" ")
