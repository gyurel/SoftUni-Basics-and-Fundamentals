input_string = input()

counter = 0
resorces_dict = {}
key = ""


while input_string != "stop":
    counter += 1
    if counter % 2 == 0:
        resorces_dict[key] += int(input_string)
    else:
        if input_string not in resorces_dict:
            resorces_dict[input_string] = 0
            key = input_string
        else:
            key = input_string

    input_string = input()



for key, val in resorces_dict.items():
    print(f"{key} -> {val}")
