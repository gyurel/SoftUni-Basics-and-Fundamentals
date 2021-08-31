factor = int(input())
count = int(input())

list = []

for i in range(1, count + 1):
    num = factor * i
    list.append(num)

print(list)
