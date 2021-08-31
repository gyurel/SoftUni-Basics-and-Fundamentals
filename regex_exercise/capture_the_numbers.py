import re

pattern = r"[0-9]+"

test_list = []
input_string = input()


while input_string != "":

    matches = re.findall(pattern, input_string)

    for match in matches:
        test_list.append(match)

    input_string = input()

print(' '.join(test_list))
