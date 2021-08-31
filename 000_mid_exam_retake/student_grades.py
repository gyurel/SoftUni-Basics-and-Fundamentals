n = int(input())

students_list = []

for i in range(n):
    current_name = input()
    current_grade = float(input())
    current_list = [current_name, current_grade]
    students_list.append(current_list)

students_list = sorted(students_list, key= lambda x: (x[1], x[0]))

values_list = sorted(list(set([el[1] for el in students_list])), key= lambda x: x)

second_lowest = values_list[1]

for el in students_list:
    if el[1] == second_lowest:
        print(el[0])
