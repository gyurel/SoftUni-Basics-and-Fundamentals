month = input()
nights = int(input())

sum_studio = 0
sum_apartment = 0

if month == "May" or month == "October":
    if nights <= 7:
        sum_studio = nights * 50
        sum_apartment = nights * 65
    elif 7 < nights <= 14:
        sum_studio = nights * 50 * 0.95
        sum_apartment = nights * 65
    elif 14 < nights:
        sum_studio = nights * 50 * 0.7
        sum_apartment = nights * 65 * 0.9
elif month == "June" or month == "September":
    if 14 < nights:
        sum_studio = nights * 75.20 * 0.8
        sum_apartment = nights * 68.70 * 0.9
    else:
        sum_studio = nights * 75.20
        sum_apartment = nights * 68.70
elif month == "July" or month == "August":
    if 14 < nights:
        sum_studio = nights * 76
        sum_apartment = nights * 77 * 0.9
    else:
        sum_studio = nights * 76
        sum_apartment = nights * 77

print(f"Apartment: {sum_apartment:.2f} lv.")
print(f"Studio: {sum_studio:.2f} lv.")
