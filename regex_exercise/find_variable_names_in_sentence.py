import re

input_string = input()

pattern = r"\b\_(?P<var_name>[A-Za-z0-9]+)\b"
match_list = []

matches = re.finditer(pattern, input_string)

for match in matches:
    match_list.append(match.group('var_name'))

print(','.join(match_list))
