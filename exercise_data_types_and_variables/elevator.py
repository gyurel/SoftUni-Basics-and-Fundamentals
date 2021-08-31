number_persons = int(input())
capacity = int(input())

full_courses = number_persons // capacity
last_course_number = number_persons % capacity

if full_courses == 0:
    print("All the persons fit inside the elevator.")
    print("Only one course is needed.")
    exit
elif last_course_number == 0:
    print(f"{full_courses} courses * {capacity} people")
else:
    print(f"{full_courses} courses * {capacity} people")
    print(f"+ 1 course * {last_course_number} persons")
