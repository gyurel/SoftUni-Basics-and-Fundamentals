input_string = input()

encrypted_string = ""

for i in range(len(input_string)):
    ascii_code = ord(input_string[i])
    encrypted_char = chr(ascii_code + 3)
    encrypted_string += encrypted_char

print(encrypted_string)
