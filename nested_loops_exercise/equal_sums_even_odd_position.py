num1 = int(input())
num2 = int(input())

for i in range(num1, num2+1):
    units = i % 10
    tens = i // 10 % 10
    hundreds = i // 100 % 10
    thousands = i // 1000 % 10
    ten_thousands = i // 10000 % 10
    hundred_thousands = i // 100000 % 10
    sum_even = units + hundreds + ten_thousands
    sum_odd = tens + thousands + hundred_thousands
    if sum_even == sum_odd:
        print(f"{i} ", end="")
