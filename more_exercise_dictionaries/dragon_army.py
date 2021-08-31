def dragon_dispersion(d_type, d_name, d_damage, d_health, d_armor, d_type_name_stat_dict, d_type_stat_dict):

    if d_damage == "null":
        d_damage = '45'
    if d_health == "null":
        d_health = '250'
    if d_armor == "null":
        d_armor = '10'

    d_damage = int(d_damage)
    d_health = int(d_health)
    d_armor = int(d_armor)

    if d_type not in d_type_name_stat_dict:
        d_type_name_stat_dict[d_type] = {d_name: [d_damage, d_health, d_armor]}
        d_type_stat_dict[d_type] = [d_damage, d_health, d_armor]
    elif d_name not in d_type_name_stat_dict[d_type]:
        d_type_name_stat_dict[d_type][d_name] = [d_damage, d_health, d_armor]
        d_type_stat_dict[d_type][0] += d_damage
        d_type_stat_dict[d_type][1] += d_health
        d_type_stat_dict[d_type][2] += d_armor
    else:
        d_type_stat_dict[d_type][0] -= d_type_name_stat_dict[d_type][d_name][0]
        d_type_stat_dict[d_type][1] -= d_type_name_stat_dict[d_type][d_name][1]
        d_type_stat_dict[d_type][2] -= d_type_name_stat_dict[d_type][d_name][2]

        d_type_name_stat_dict[d_type][d_name] = [d_damage, d_health, d_armor]

        d_type_stat_dict[d_type][0] += d_damage
        d_type_stat_dict[d_type][1] += d_health
        d_type_stat_dict[d_type][2] += d_armor

    return d_type_name_stat_dict


type_name_statistics_dict = {}
type_stat_dict = {}

n = int(input())

for i in range(n):

    input_string = input()
    type, name, damage, health, armor = input_string.split()

    type_name_statistics_dict = dragon_dispersion(type, name, damage, health, armor, type_name_statistics_dict, type_stat_dict)


for typ, value_list in type_name_statistics_dict.items():
    print(f"{typ}::({type_stat_dict[typ][0] / len(type_name_statistics_dict[typ]):.2f}/{type_stat_dict[typ][1] / len(type_name_statistics_dict[typ]):.2f}/{type_stat_dict[typ][2] / len(type_name_statistics_dict[typ]):.2f})")
    for name, stats in sorted(value_list.items(), key=lambda x: x[0]):
        print(f"-{name} -> damage: {stats[0]}, health: {stats[1]}, armor: {stats[2]}")
