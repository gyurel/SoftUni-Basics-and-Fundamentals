n = int(input())


for number in range(1111, 10000):
    counter = 0
    for digit in str(number)[0: 4]:
        if int(digit) == 0:
            pass
        elif n % int(digit) == 0:
            counter += 1
    if counter == 4:
        print(f"{number}", end=" ")
