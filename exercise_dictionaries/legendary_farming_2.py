key_materails_dict = {'shards': 0, 'fragments': 0, 'motes': 0}
junnk_dict = {}
legendary_item_obtained = ''

while legendary_item_obtained == '':

    input_string = input().split()

    for i in range(0, len(input_string), 2):
        mat_qty = int(input_string[i])
        mat_name = input_string[i + 1].lower()

        if mat_name in key_materails_dict:
            key_materails_dict[mat_name] += mat_qty

            if key_materails_dict[mat_name] >= 250:
                if mat_name == "shards":
                    legendary_item_obtained = 'Shadowmourne'
                    key_materails_dict[mat_name] -= 250
                    break

                elif mat_name == "fragments":
                    legendary_item_obtained = 'Valanyr'
                    key_materails_dict[mat_name] -= 250
                    break

                elif mat_name == "motes":
                    legendary_item_obtained = 'Dragonwrath'
                    key_materails_dict[mat_name] -= 250
                    break

        else:
            if mat_name in junnk_dict:
                junnk_dict[mat_name] += mat_qty
            else:
                junnk_dict[mat_name] = mat_qty


print(f'{legendary_item_obtained} obtained!')

# sorted_junk = sorted(junnk_dict.items(), key= lambda kvp: (kvp[0]))

for key_mat_name, key_mat_qty in sorted(key_materails_dict.items(), key= lambda kvp: (-kvp[1], kvp[0])):
    print(f'{key_mat_name}: {key_mat_qty}')

for junk_name, junk_qty in sorted(junnk_dict.items(), key= lambda kvp: (kvp[0])):
    print(f'{junk_name}: {junk_qty}')
