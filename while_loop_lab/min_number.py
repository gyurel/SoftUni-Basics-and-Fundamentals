import sys
num = input()

min_num = sys.maxsize

while num != "Stop":
    if int(num) < min_num:
        min_num = int(num)
        num = input()
    else:
        num = input()

print(min_num)
