def sum_numbers(num1, num2):
    sum_result = num1 + num2

    return sum_result


def subtract(sum_nr, num3):
    result = sum_nr - num3

    return result

def add_and_subtract(num1, num2, num3):
    sum_nr = sum_numbers(num1, num2)
    result = subtract(sum_nr, num3)

    return result

num1 = int(input())
num2 = int(input())
num3 = int(input())

print(add_and_subtract(num1, num2, num3))
