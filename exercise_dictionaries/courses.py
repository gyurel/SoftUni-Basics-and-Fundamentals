input_strint = input()

register_dict = {}

while input_strint != "end":

    command = input_strint.split(' : ')

    course_name = command[0]
    student_name = command[1]

    if course_name not in register_dict:
        register_dict[course_name] = [student_name]
    else:
        register_dict[course_name].append(student_name)

    input_strint = input()

for key_course_name, val_students_names in sorted(register_dict.items(), key= lambda kvp: (-len(kvp[1]))):
    print(f"{key_course_name}: {len(val_students_names)}")
    val_students_names.sort()
    for val in val_students_names:
        print(f"-- {val}")
