import re

input_string = input()
match_list = []


pattern = r"(?P<email>(?P<user>(^|(?<=\s))[A-Za-z0-9]+[\._-]?[A-Za-z0-9]+)@(?P<host>[A-Za-z]+\-?[A-Za-z]+(\.[A-Za-z]+\-?[A-Za-z]+)+))"

matches = re.finditer(pattern, input_string)

for match in matches:
    match_list.append(match.group('email'))

print(*match_list, sep='\n')
