input_str = input()

languages_dict = {}
student_points_dict = {}
banned_users_list = []

while input_str != "exam finished":

    command = input_str.split("-")

    if "banned" in command:
        student_name = command[0]

        banned_users_list.append(student_name)
        if student_name in student_points_dict:
            del student_points_dict[student_name]
        input_str = input()
        continue

    student_name = command[0]
    language = command[1]
    points = int(command[2])

    if not student_name in banned_users_list:

        if student_name in student_points_dict:
            if points > student_points_dict[student_name]:
                student_points_dict[student_name] = points
        else:
            student_points_dict[student_name] = points

        if language in languages_dict:
            languages_dict[language] += 1
        else:
            languages_dict[language] = 1

    input_str = input()

print("Results:")

for key_student_name, key_student_result in sorted(student_points_dict.items(), key= lambda kvp: (-kvp[1], kvp[0])):
    print(f"{key_student_name} | {key_student_result}")

print("Submissions:")

for key_language_name, key_submissions in sorted(languages_dict.items(), key= lambda kvp: (-kvp[1], kvp[0])):
    print(f"{key_language_name} - {key_submissions}")
