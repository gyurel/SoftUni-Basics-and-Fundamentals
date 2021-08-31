contests_info_dict = {}

input_str = input()

while input_str != "no more time":

    student_name, contest_name, points = input_str.split(" -> ")
    points = int(points)

    if contest_name not in contests_info_dict:
        contests_info_dict[contest_name] = {student_name: points}
    elif student_name not in contests_info_dict[contest_name]:
        contests_info_dict[contest_name][student_name] = points
    else:
        if points > contests_info_dict[contest_name][student_name]:
            contests_info_dict[contest_name][student_name] = points

    input_str = input()

contests_info_dict_sorted = {contest: {name: st_points for name, st_points in sorted(student_info.items(), key=lambda kvp: (-kvp[1], kvp[0]))}\
                             for contest, student_info in sorted(contests_info_dict.items(), key= lambda kvp: -len(kvp[1]))}

for contest, student_points in contests_info_dict_sorted.items():
    print(f"{contest}: {len(student_points)} participants")
    rank = 0
    for user, point in student_points.items():
        rank += 1
        print(f"{rank}. {user} <::> {point}")


individual_standings = {}

for contest, values in contests_info_dict_sorted.items():
    for names, char in values.items():
        if names not in individual_standings:
            individual_standings[names] = char
        else:
            individual_standings[names] += char

individual_standings_sorted = {name: points for name, points in sorted(individual_standings.items(), key=lambda kvp: (-kvp[1], kvp[0]))}

print("Individual standings:")

counter = 0
for user, point in individual_standings_sorted.items():
    counter += 1
    print(f"{counter}. {user} -> {point}")
