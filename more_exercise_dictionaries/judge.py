contests_info_dict = {}

input_str = input()

while input_str != "no more time":

    student_name, contest_name, points = input_str.split(" -> ")
    points = int(points)

    # contest_name = contest_info_list[1]
    # student_name = contest_info_list[0]
    # points = int(contest_info_list[2])

    if contest_name not in contests_info_dict:
        contests_info_dict[contest_name] = {student_name: points}
    elif student_name not in contests_info_dict[contest_name]:
        contests_info_dict[contest_name][student_name] = points
    else:
        if points > contests_info_dict[contest_name][student_name]:
            contests_info_dict[contest_name][student_name] = points

    input_str = input()

standings_dict = {}

for contest, contest_data in contests_info_dict.items():
    print(f"{contest}: {len(contest_data)} participants")
    rank = 0

    for st_name, st_points in sorted(contest_data.items(), key=lambda kvp: (-kvp[1], kvp[0])):
        rank += 1
        print(f"{rank}. {st_name} <::> {st_points}")

    for name, point in contest_data.items():
        if name not in standings_dict:
            standings_dict[name] = point
        else:
            standings_dict[name] += point

print(f"Individual standings:")




standings_rank = 0

for key, val in sorted(standings_dict.items(), key=lambda kvp: (-kvp[1], kvp[0])):
    standings_rank += 1

    print(f"{standings_rank}. {key} -> {val}")
