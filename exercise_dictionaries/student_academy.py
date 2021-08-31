n = int(input())

students_register = {}
new_studetnts_reg_dict = {}

for i in range(n):

    student = input()
    grade = float(input())

    if student not in students_register:
        students_register[student] = [grade]

    else:
        students_register[student].append(grade)


for key, val in students_register.items():
    if sum(val) / len(val) >= 4.50:
        new_studetnts_reg_dict[key] = val

for key_student, val_grades in sorted(new_studetnts_reg_dict.items(), key= lambda kvp: (-(sum(kvp[1]) / len(kvp[1])))):
    print(f"{key_student} -> {sum(val_grades) / len(val_grades):.2f}")
