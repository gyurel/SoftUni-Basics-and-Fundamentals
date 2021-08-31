input_string = input().split(",")

for i in range(len(input_string)):
    current_el = input_string[i]
    input_string.remove(current_el)
    current_el = current_el.strip()
    input_string.insert(i, current_el)


special_symbols = "@#$^"

for i in range(len(input_string)):
    current_element = input_string[i]

    if len(current_element) < 20 or len(current_element) > 20:
        print("invalid ticket")
        continue

    half_size = 10
    left_part = current_element[:10]
    right_part = current_element[10:]
    longest_left_string = 0
    longest_right_string = 0
    counter_left_longest = 0
    counter_right_longest = 0
    current_spec_char_left = ''
    current_spec_char_right = ''

    for j in range(half_size):
        current_left_char = left_part[j]
        current_right_char = right_part[j]

        if current_left_char in special_symbols:
            counter_left_longest += 1
            if counter_left_longest > longest_left_string:
                current_spec_char_left = current_left_char
                longest_left_string = counter_left_longest
        else:
            counter_left_longest = 0


        if current_right_char in special_symbols:
            counter_right_longest += 1
            if counter_right_longest > longest_right_string:
                current_spec_char_right = current_right_char
                longest_right_string = counter_right_longest
        else:
            counter_right_longest = 0


    if current_spec_char_left == current_spec_char_right and current_spec_char_left != '' and current_spec_char_right != '':
        spec_char = current_spec_char_left
        if longest_left_string == 10 and longest_right_string == 10:
            print(f'ticket "{current_element}" - {longest_left_string}{spec_char} Jackpot!')
        elif 6 <= longest_left_string <= 9 and 6 <= longest_right_string <= 9:
            print(f'ticket "{current_element}" - {longest_left_string}{spec_char}')
        else:
            print(f'ticket "{current_element}" - no match')
    else:
        print(f'ticket "{current_element}" - no match')
