import re

pattern_name = r"[A-Za-z]+"
pattern_distance = r"[0-9]"

match_names = {}


name_list = input().split(", ")


command = input()

while command != "end of race":

    matches = re.finditer(pattern_name, command)
    matches_dig = re.finditer(pattern_distance, command)

    current_name = ""
    current_str = []

    for match in matches:
        current_str.append(match.group())
    current_name = ''.join(current_str)
    if current_name in name_list:
        if current_name not in match_names:
            match_names[current_name] = 0

    current_dig_list = []

    for match in matches_dig:
        current_dig_list.append(int(match.group()))
    if current_name not in match_names:
        pass
    else:
        match_names[current_name] += sum(current_dig_list)

    command = input()

match_names = {key: val for key, val in sorted(match_names.items(), key=lambda x: -x[1])}

suffixes = ["st", "nd", "rd"]

counter = 0
for key, val in match_names.items():
    counter += 1
    print(f"{counter}{suffixes[counter - 1]} place: {key}")

    if counter == 3:
        break
