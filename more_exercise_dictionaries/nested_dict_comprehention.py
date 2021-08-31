licenses_reg = {'driving license C': {'Pesho': 5, 'Mimi': 6}, 'driving license B': {'Pesho': 3, 'Gosho': 4, 'Stamat': 2}}


sorted_licenses_reg = {key_license: {key_name: key_char for key_name, key_char in sorted(key_dict.items(), key=lambda kvp: -kvp[1])} \
                       for key_license, key_dict in sorted(licenses_reg.items(), key=lambda kvp: -len(kvp[1]))}

print(sorted_licenses_reg)
