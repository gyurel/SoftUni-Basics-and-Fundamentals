number = int(input())

for i in range(1, number+1):
    print()
    for x in range(0, i):
        print("*", end="")
for i in range(number - 1, 0, -1):
    print()
    for x in range(0, i):
        print("*", end="")
