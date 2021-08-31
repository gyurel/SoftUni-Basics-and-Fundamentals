name = input()

character = float(input())
year = 1
fails = 0
sum_characters = 0
average_character = 0

while year <= 12:
    if character >= 4 and fails <= 1:
        year += 1
        sum_characters += character
        average_character = sum_characters / 12
        if year == 13:
            print(f"{name} graduated. Average grade: {average_character:.2f}")
            break
        else:
            character = float(input())
    elif character < 4 and fails <= 1:
        fails += 1
    else:
        print(f"{name} has been excluded at {year} grade")
        break
