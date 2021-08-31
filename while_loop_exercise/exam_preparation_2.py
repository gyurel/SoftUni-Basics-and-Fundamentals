count_poor_grades = int(input())

poor_grades_counter = 0
last_problem_name = ""
sum_grades = 0
grades_counter = 0
grades_mean_value = 0
has_failed = True

while poor_grades_counter < count_poor_grades:
    problem_name = input()
    if problem_name == "Enough":
        has_failed = False
        break

    grade = int(input())
    if grade <= 4:
        poor_grades_counter += 1
    grades_counter += 1
    sum_grades += grade
    last_problem_name = problem_name

if has_failed:
    print(f"You need a break, {poor_grades_counter} poor grades.")
else:
    grades_mean_value = sum_grades / grades_counter
    print(f"Average score: {grades_mean_value:.2f}")
    print(f"Number of problems: {grades_counter}")
    print(f"Last problem: {last_problem_name}")
