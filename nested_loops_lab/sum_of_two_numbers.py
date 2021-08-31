num1 = int(input())
num2 = int(input())
magic_number = int(input())

is_found = False
counter = 0

for number1 in range(num1, num2+1):
    for number2 in range(num1, num2+1):
        sum = number1 + number2
        counter += 1
        if sum == magic_number:
            is_found = True
            print(f"Combination N:{counter} ({number1} + {number2} = {magic_number})")
            break
    if is_found:
        break
else:
    print(f"{counter} combinations - neither equals {magic_number}")
