number_joury = int(input())
presentation_name = input()

total_sum_grades = 0
total_counter_grades = 0

while presentation_name != "Finish":
    grade = float(input())
    current_sum_grades = 0
    current_counter_grades = 0
    for i in range(1, number_joury+1):
        current_sum_grades += grade
        total_sum_grades += grade
        current_counter_grades += 1
        total_counter_grades += 1
        if i == number_joury:
            print(f"{presentation_name} - {current_sum_grades/current_counter_grades:.2f}.")
            presentation_name = input()
            break
        grade = float(input())
else:
    print(f"Student's final assessment is {total_sum_grades/total_counter_grades:.2f}.")
