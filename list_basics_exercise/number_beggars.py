nums_str = input().split(", ")
beggars = int(input())

print_list = [0] * beggars

for i in range(len(nums_str)):
    index = i % beggars
    print_list[index] += int(nums_str[i])

print(print_list)
