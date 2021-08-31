number1 = int(input())
number2 = int(input())
operator = input()

total_sum = 0
subtraction_result = 0
multiplication_result = 0
division_result = 0
modulus_result = 0

if operator == "+":
    total_sum = number2 + number1
    if total_sum % 2 == 0:
        oddeven = "even"
    else:
        oddeven = "odd"
    print(f"{number1} {operator} {number2} = {total_sum} - {oddeven}")

elif operator == "-":
    subtraction_result = number1 - number2
    if subtraction_result % 2 == 0:
        oddeven = "even"
    else:
        oddeven = "odd"
    print(f"{number1} {operator} {number2} = {subtraction_result} - {oddeven}")
elif operator == "*":
    multiplication_result = number1 * number2
    if multiplication_result % 2 == 0:
        oddeven = "even"
    else:
        oddeven = "odd"
    print(f"{number1} {operator} {number2} = {multiplication_result} - {oddeven}")
# •	Ако операцията е събиране, изваждане или умножение:
# o	 "{N1} {оператор} {N2} = {резултат} - {even/odd}"
# •	Ако операцията е деление:
# o	"{N1} / {N2} = {резултат}" - резултат, форматиран до втория знак след десетичната запетая
# •	Ако операцията е модулно деление:
# o	"{N1} % {N2} = {остатък}"
# •	В случай на деление с 0 (нула):
# o	"Cannot divide {N1} by zero"

elif operator == "/":
    if number2 == 0:
        print(f"Cannot divide {number1} by zero")
    else:
        division_result = number1 / number2
        print(f"{number1} / {number2} = {division_result:.2f}")
elif operator == "%":
    if number2 == 0:
        print(f"Cannot divide {number1} by zero")
    else:
        modulus_result = number1 % number2
        print(f"{number1} % {number2} = {modulus_result}")
