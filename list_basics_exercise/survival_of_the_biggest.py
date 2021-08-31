integers_str = input().split()
n = int(input())

integers_list = []

for i in range(len(integers_str)):
    integers_list.append(int(integers_str[i]))

for _ in range(n):
    integers_list.remove(min(integers_list))

for _ in range(len(integers_list)):
    if _ < len(integers_list) - 1:
        print(integers_list[_], end=", ")
    else:
        print(integers_list[_])
