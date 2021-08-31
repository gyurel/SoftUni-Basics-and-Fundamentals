import sys


def return_smallest(num1, num2, num3):
    nums_list = [num1, num2, num3]
    smallest_num = sys.maxsize

    for element in nums_list:
        if element < smallest_num:
            smallest_num = element

    return smallest_num


num1 = int(input())
num2 = int(input())
num3 = int(input())


print(return_smallest(num1, num2, num3))
