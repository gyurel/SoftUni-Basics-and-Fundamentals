count_num = int(input())
sum_even = 0
sum_odd = 0

for i in range(1, count_num + 1):
    num = int(input())
    if i % 2 == 0:
        sum_even += num
    else:
        sum_odd += num

if sum_odd == sum_even:
    print(f"Yes\nSum = {sum_odd} ")
else:
    diff = abs(sum_odd - sum_even)
    print(f"No\nDiff = {diff} ")
