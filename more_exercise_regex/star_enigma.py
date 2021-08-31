import re

look_up_chars = ['s', 't', 'a', 'r']
pattern = r"^[^-@!:>]*@(?P<planet>[A-Za-z]+)[^-@!:>]*:(?P<population>\d+)[^-@!:>]*!(?P<attack_type>[A-Z])![^-@!:>]*->(?P<soldier_count>\d+)[^-@!:>]*$"

attack_list = []
destruction_list = []

n = int(input())

for i in range(n):

    input_string = list(input())

    correction_counter = 0
    clean_string = ""

    for el in input_string:

        if el.lower() in look_up_chars:
            correction_counter += 1

    for i in range(len(input_string)):
        new_char = chr(ord(input_string[i]) - correction_counter)
        clean_string += new_char

    planet_attack = re.match(pattern, clean_string)

    if planet_attack == None:
        continue

    planet = planet_attack.group('planet')
    population = planet_attack.group('population')
    attack_type = planet_attack.group('attack_type')
    soldier_count = planet_attack.group('soldier_count')

    if attack_type == "A":
        attack_list.append(planet)
    elif attack_type == "D":
        destruction_list.append(planet)

attack_list = [el for el in sorted(attack_list, key=lambda x: x)]
destruction_list = [el for el in sorted(destruction_list, key=lambda x: x)]

print(f"Attacked planets: {len(attack_list)}")
for el in attack_list:
    print(f"-> {el}")
print(f"Destroyed planets: {len(destruction_list)}")
for el in destruction_list:
    print(f"-> {el}")
