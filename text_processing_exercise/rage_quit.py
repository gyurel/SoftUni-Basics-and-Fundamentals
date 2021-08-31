input_string = list(input())

result_str = ""
unique_symbols = []

last_digit_index = 0


for i in range(len(input_string)):
    current_index = i
    current_char = input_string[current_index]

    if not current_char.isdigit():
        pass
    elif current_char.isdigit():
        if not current_index == len(input_string) - 1:
            if input_string[i + 1].isdigit():
                multiplication_string = (''.join(input_string[last_digit_index:current_index]) * int(current_char + input_string[i + 1])).upper()
                result_str += multiplication_string
                last_digit_index = current_index + 2

        multiplication_string = (''.join(input_string[last_digit_index:current_index]) * int(current_char)).upper()
        result_str += multiplication_string
        last_digit_index = current_index + 1

for el in result_str:
    if el not in unique_symbols:
        unique_symbols.append(el)


print(f"Unique symbols used: {len(unique_symbols)}")
print(result_str)
