input_string = list(input())

result_str = ""

explosion_power = 0
i = 0

while i < len(input_string):

    current_char = input_string[i]

    if current_char == ">":
        result_str += current_char
        explosion_power += int(input_string[i + 1])
    else:
        if explosion_power > 0:
            explosion_power -= 1
        else:
            result_str += current_char

    i += 1

print(result_str)
