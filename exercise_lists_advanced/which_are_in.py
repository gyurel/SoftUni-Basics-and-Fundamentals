def string_in_string(str_1, str_2):

    new_lsit = []

    for str in str_1:
        current_str = str
        for el in str_2:
            if current_str in el:
                new_lsit.append(current_str)
                break
    return new_lsit


str_1 = input().split(", ")
str_2 = input().split(", ")

a = string_in_string(str_1, str_2)
print(a)
