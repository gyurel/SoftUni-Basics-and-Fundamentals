input_string = input().split(",")

for i in range(len(input_string)):
    current_element = input_string[i]
    input_string.remove(current_element)
    current_element = current_element.strip()
    input_string.insert(i, current_element)


for i in range(len(input_string)):
    current_element = input_string[i]
    current_collection_left = ''
    current_collection_right = ''

    if len(current_element) == 20:

        half_size = int(len(current_element) / 2)
        left_part = current_element[0:half_size]
        right_part = current_element[half_size:len(current_element)]

        # '@', '#', '$' and '^'

        if '@' in left_part and '@' in right_part:

            for j in range(len(left_part)):
                current_char_left = left_part[j]
                current_char_right = right_part[j]

                if current_char_left == '@':
                    current_collection_left += '@'

                if current_char_right == '@':
                    current_collection_right += '@'

            if len(current_collection_left) == len(current_collection_right):

                if len(current_collection_left) == 10 and len(current_collection_right) == 10:
                    print(f'ticket "{current_element}" - {len(current_collection_left)}@ Jackpot!')
                    # "ticket "{ticket}" - {match length}{match symbol} Jackpot!"

                elif 6 <= len(current_collection_left)  <=  9 and 6 <= len(current_collection_right)  <=  9:
                    print(f'ticket "{current_element}" - {len(current_collection_left)}@')

                else:
                    print(f'ticket "{current_element}" - no match')

            else:
                print(f'ticket "{current_element}" - no match')

        elif '#' in left_part and '#' in right_part:

            for j in range(len(left_part)):
                current_char_left = left_part[j]
                current_char_right = right_part[j]

                if current_char_left == '#':
                    current_collection_left += '#'

                if current_char_right == '#':
                    current_collection_right += '#'

            if len(current_collection_left) == len(current_collection_right):

                if len(current_collection_left) == 10 and len(current_collection_right) == 10:
                    print(f'ticket "{current_element}" - {len(current_collection_left)}# Jackpot!')
                    # "ticket "{ticket}" - {match length}{match symbol} Jackpot!"

                elif 6 <= len(current_collection_left) <= 9 and 6 <= len(current_collection_right) <= 9:
                    print(f'ticket "{current_element}" - {len(current_collection_left)}#')

                else:
                    print(f'ticket "{current_element}" - no match')

            else:
                print(f'ticket "{current_element}" - no match')

        elif '$' in left_part and '$' in right_part:

            for j in range(len(left_part)):
                current_char_left = left_part[j]
                current_char_right = right_part[j]

                if current_char_left == '$':
                    current_collection_left += '$'

                if current_char_right == '$':
                    current_collection_right += '$'

            if len(current_collection_left) == len(current_collection_right):

                if len(current_collection_left) == 10 and len(current_collection_right) == 10:
                    print(f'ticket "{current_element}" - {len(current_collection_left)}$ Jackpot!')
                    # "ticket "{ticket}" - {match length}{match symbol} Jackpot!"

                elif 6 <= len(current_collection_left)  <=  9 and 6 <= len(current_collection_right)  <=  9:
                    print(f'ticket "{current_element}" - {len(current_collection_left)}$')

                else:
                    print(f'ticket "{current_element}" - no match')

            else:
                print(f'ticket "{current_element}" - no match')

        elif '^' in left_part and '^' in right_part:

            for j in range(len(left_part)):
                current_char_left = left_part[j]
                current_char_right = right_part[j]

                if current_char_left == '^':
                    current_collection_left += '^'

                if current_char_right == '^':
                    current_collection_right += '^'

            if len(current_collection_left) == len(current_collection_right):

                if len(current_collection_left) == 10 and len(current_collection_right) == 10:
                    print(f'ticket "{current_element}" - {len(current_collection_left)}^ Jackpot!')
                    # "ticket "{ticket}" - {match length}{match symbol} Jackpot!"

                elif 6 <= len(current_collection_left)  <=  9 and 6 <= len(current_collection_right)  <=  9:
                    print(f'ticket "{current_element}" - {len(current_collection_left)}@')

                else:
                    print(f'ticket "{current_element}" - no match')

            else:
                print(f'ticket "{current_element}" - no match')

        else:
            print(f'ticket "{current_element}" - no match')


    else:
        print("invalid ticket")
