import sys
num = input()

max_num = -sys.maxsize

while num != "Stop":
    if int(num) > max_num:
        max_num = int(num)
        num = input()
    else:
        num = input()

print(max_num)
