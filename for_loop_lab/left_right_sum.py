count_num = int(input())
sum1 = 0
sum2 = 0

for i in range(0, count_num):
    num = int(input())
    sum1 += num

for i in range(0, count_num):
    num = int(input())
    sum2 += num

if sum1 == sum2:
    print(f"Yes, sum = {sum1}")
elif sum1 != sum2:
    diff = abs(sum1 - sum2)
    print(f"No, diff = {diff}")
