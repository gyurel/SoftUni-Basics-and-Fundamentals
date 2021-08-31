number_of_studens = int(input())

# между 2.00 и 2.99, между 3.00 и 3.99, между 4.00 и 4.99, 5.00 или повече.
total_counter = 0
counter1 = 0
counter2 = 0
counter3 = 0
counter4 = 0
sum_grades = 0

for grade in range(0, number_of_studens):
    grade = float(input())
    sum_grades += grade
    total_counter += 1
    if 2.00 <= grade <= 2.99:
        counter1 += 1
    elif 3.00 <= grade <= 3.99:
        counter2 += 1
    elif 4.00 <= grade <= 4.99:
        counter3 += 1
    elif 5.00 <= grade:
        counter4 += 1

print(f"Top students: {counter4/total_counter*100:.2f}%")
print(f"Between 4.00 and 4.99: {counter3/total_counter*100:.2f}%")
print(f"Between 3.00 and 3.99: {counter2/total_counter*100:.2f}%")
print(f"Fail: {counter1/total_counter*100:.2f}%")
print(f"Average: {sum_grades/total_counter:.2f}")
