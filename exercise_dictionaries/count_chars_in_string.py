input_string = input()

chars_dict = {}

for char in input_string:
    if char != " ":
        if char not in chars_dict:
            chars_dict[char] = 1
        else:
            chars_dict[char] += 1
    else:
        continue

# print(f"{key} -> {val}" for key, val in chars_dict.items())

for key, val in chars_dict.items():
    print(f"{key} -> {val}")
