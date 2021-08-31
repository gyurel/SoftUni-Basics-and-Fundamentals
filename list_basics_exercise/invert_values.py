string_numbers = input().split()

list_opposite_nums = []

for num in string_numbers:
    current_num = num
    current_num = int(current_num) * -1
    list_opposite_nums.append(current_num)

print(list_opposite_nums)
