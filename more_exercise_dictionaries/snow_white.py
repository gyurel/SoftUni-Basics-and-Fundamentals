input_string = input()

dwarf_info_dict = {}

while input_string != "Once upon a time":

    dwarf_info = input_string.split(" <:> ")
    dwarf_name = dwarf_info[0]
    dwarf_hat_color = dwarf_info[1]
    dwarf_physics = int(dwarf_info[2])

    if dwarf_hat_color not in dwarf_info_dict:
        dwarf_info_dict[dwarf_hat_color] = {dwarf_name: dwarf_physics}

    elif dwarf_name not in dwarf_info_dict[dwarf_hat_color]:
        dwarf_info_dict[dwarf_hat_color][dwarf_name] = dwarf_physics
    else:
        if dwarf_physics > dwarf_info_dict[dwarf_hat_color][dwarf_name]:
            dwarf_info_dict[dwarf_hat_color][dwarf_name] = dwarf_physics

    input_string = input()


dwarf_info_list = [(color, name, pysics, len(name_pys)) for color, name_pys in dwarf_info_dict.items() for name, pysics in name_pys.items()]

dwarf_info_list = sorted(dwarf_info_list, key=lambda x: (x[2], x[3]), reverse= True)

for el in dwarf_info_list:
    print(f"({el[0]}) {el[1]} <-> {el[2]}")
