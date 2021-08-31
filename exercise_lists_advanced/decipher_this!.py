def decipher_code(secret_message):

    deciphered_message = []

    for el in secret_message:
        current_numeric_part = [digit for digit in el if digit.isdigit()]
        current_str_part = [letter for letter in el if letter.isalpha()]
        current_str_part[0], current_str_part[-1] = current_str_part[-1], current_str_part[0]
        current_deciphered_element = chr(int("".join(current_numeric_part))) + "".join(current_str_part)
        deciphered_message.append(current_deciphered_element)

    return deciphered_message

secret_message = input().split()
a = decipher_code(secret_message)

for el in a:
    print(el, end=" ")
