import re

deamon_book = {}
damage_pattern = r"[-+]?[0-9]+\.?[0-9]*"
operationals_pattern = r"[*/]"
validity_pattern = r"^[^\s,]*$"


input_string = [el.lstrip() for el in input().split(", ")]

for el in input_string:

    if re.match(validity_pattern, el) == None:
        continue

    health = 0
    for char in el:
        if char.isalpha():
            health += ord(char)
    if health == 0:
        continue

    deamon_book[el] = {'Health': health, 'Damage': 0}

    chars_in_name = re.finditer(damage_pattern, el)

    sum_damage = 0
    for match in chars_in_name:
        current_dmg = float(match.group())
        sum_damage += current_dmg

    operationals = re.finditer(operationals_pattern, el)

    list_operationals = []
    for oper in operationals:
        operand = oper.group()
        list_operationals.append(operand)

    if len(list_operationals) != 0:
        for opr in list_operationals:
            if opr == "*":
                sum_damage *= 2
            elif opr == "/":
                sum_damage /= 2

    deamon_book[el]['Damage'] = sum_damage

deamon_book = {key: val for key, val in sorted(deamon_book.items(), key=lambda x: x[0])}

for k, v in deamon_book.items():
    print(f"{k} - {v['Health']} health, {v['Damage']:.2f} damage")
