input_string = input().split(", ")

valid_usernames = []
current_username = ""
is_valid = True

for el in input_string:
    is_valid = True
    if 3 <= len(el) <= 16:

        for char in el:
            if char.isdigit():
                current_username += char
            elif char.isalpha():
                current_username += char
            elif char == "-":
                current_username += char
            elif char == "_":
                current_username += char
            else:
                current_username = ""
                is_valid = False
                break

        if is_valid:
            valid_usernames.append(current_username)
            current_username = ""
    else:
        continue

print(*valid_usernames, sep='\n')
