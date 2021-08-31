def factorial_devision(int1, int2):

    factorial_list1 = []
    factorial_list2 = []
    product1 = int1
    product2 = int2

    factorial_list1 = [element for element in range(int1 - 1, 0, - 1)]
    factorial_list2 = [element for element in range(int2 - 1, 0, - 1)]

    # product1 = lambda int1: int1 * element for element in factorial_list1
    # product2 = lambda int2: int2 * element for element in factorial_list2

    for i in range(len(factorial_list1)):
        product1 *= factorial_list1[i]

    for i in range(len(factorial_list2)):
        product2 *= factorial_list2[i]

    result = product1 / product2

    return f"{result:.2f}"

int1 = int(input())
int2 = int(input())

print(factorial_devision(int1, int2))
