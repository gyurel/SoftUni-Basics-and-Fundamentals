import re

pattern = r"(?<=([=/]))(?P<location>[A-Z][A-Za-z]{2,})(?=(\1))"

input_string = input()

locations_iter = re.finditer(pattern, input_string)

location_list = []
for match in locations_iter:
    current_location = match.group('location')
    location_list.append(current_location)


travel_points = 0

for el in location_list:
    travel_points += len(el)

print(f"Destinations: {', '.join(location_list)}")
print(f"Travel Points: {travel_points}")
