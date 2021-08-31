def number_classificator(number_string):

    positive_nums = [el for el in number_string if int(el) >= 0]
    negative_nums = [el for el in number_string if int(el) < 0]
    even_nums = [el for el in number_string if int(el) % 2 == 0]
    odd_nums = [el for el in number_string if int(el) % 2 == 1]

    positive_nums_str = ", ".join(positive_nums)
    negative_nums_str = ", ".join(negative_nums)
    even_nums_str = ", ".join(even_nums)
    odd_nums_str = ", ".join(odd_nums)

    result = f"Positive: {positive_nums_str}\nNegative: {negative_nums_str}\nEven: {even_nums_str}\nOdd: {odd_nums_str}"

    return result

number_string = input().split(", ")
print(number_classificator(number_string))
