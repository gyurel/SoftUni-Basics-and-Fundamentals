from itertools import product

k, m = list(map(int, input().split()))

list_of_lists = []

for i in range(int(k)):
    list_info = list(map(int, input().split()))
    current_list = list_info[1:]
    for j in range(len(current_list)):
        to_power = current_list[j] ** 2
        current_list.pop(j)
        current_list.insert(j, to_power)
    list_of_lists.append(current_list)

max = 0
for P in product(*list_of_lists):
    current_max = sum(P) % m
    if current_max > max:
        max = current_max

print(max)
