def odd_and_even_sum(input_str):
    odd_sum = []
    even_sum = []
    even_sum += [int(x) for x in input_str if int(x) % 2 == 0]
    odd_sum += [int(x) for x in input_str if int(x) % 2 == 1]

    return f"Odd sum = {sum(odd_sum)}, Even sum = {sum(even_sum)}"


input_str = input()
print(odd_and_even_sum(input_str))
