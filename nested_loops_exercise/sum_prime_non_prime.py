number = input()

sum_prime = 0
sum_non_prime = 0
counter = 0


while number != "stop":
    if int(number) >= 0:
        for factor in range(1, int(number)+1):
            if int(number) % factor == 0:
                counter += 1
        if counter == 2:
            sum_prime += int(number)
        else:
            sum_non_prime += int(number)
        counter = 0
    else:
        print("Number is negative.")
    number = input()


else:
    print(f"Sum of all prime numbers is: {sum_prime}")
    print(f"Sum of all non prime numbers is: {sum_non_prime}")
