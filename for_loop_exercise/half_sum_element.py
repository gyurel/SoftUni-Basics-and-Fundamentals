import sys

max_num = -sys.maxsize
sum_elements = 0

n = int(input())

for i in range(0, n):
    num = int(input())
    if num > max_num:
        max_num = num
    sum_elements += num

#  "Yes"
# "Sum = "  + неговата стойност ,иначе печата
# "No"
#  "Diff = " + разликата между най-големия елемент и сумата на останалите (по абсолютна стойност).

if max_num == sum_elements - max_num:
    sum_rest = sum_elements - max_num
    print("Yes")
    print(f"Sum = {sum_rest}")
else:
    sum_rest = max_num - (sum_elements - max_num)
    print("No")
    print(f"Diff = {abs(sum_rest)}")
