contest_info = input()

contest_info_dict = {}

while contest_info != "end of contests":

    contest_info = contest_info.split(":")

    key = contest_info[0]
    value = contest_info[1]
    contest_info_dict[key] = value

    contest_info = input()

student_info_dict = {}

student_info = input()

while student_info != "end of submissions":

    student_info = student_info.split("=>")
    current_contest = student_info[0]
    current_password = student_info[1]
    current_student = student_info[2]
    current_points = int(student_info[3])

    if current_contest in contest_info_dict and current_password == contest_info_dict[current_contest]:

        if current_student not in student_info_dict:
            student_info_dict[current_student] = {current_contest: current_points}


        elif current_contest not in student_info_dict[current_student]:
            student_info_dict[current_student][current_contest] = current_points

        else:
            if current_points > student_info_dict[current_student][current_contest]:
                student_info_dict[current_student][current_contest] = current_points

    student_info = input()

best_name = ""
best_student_points = 0

for key, value in student_info_dict.items():
    name = key
    total_points = 0
    for key_program, key_point in value.items():
        points = key_point
        total_points += points
    if total_points > best_student_points:
        best_name = name
        best_student_points = total_points


print(f"Best candidate is {best_name} with total {best_student_points} points.\nRanking:")


for key_student_name, val_contest_points in sorted(student_info_dict.items(), key= lambda kvp: kvp[0]):
    print(f"{key_student_name}")
    for key_contest_name, val_points in sorted(val_contest_points.items(), key= lambda kvp: -kvp[1]):
        print(f"#  {key_contest_name} -> {val_points}")
