number_persons = int(input())
capacity = int(input())

full_courses = number_persons // capacity
last_course_number = number_persons % capacity

if full_courses == 0:
    print("1")
elif last_course_number == 0:
    print(full_courses)
else:
    print(full_courses + 1)
