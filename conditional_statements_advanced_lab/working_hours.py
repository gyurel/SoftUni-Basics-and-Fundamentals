hour = int(input())
day = input()
open = ""

if 10 <= hour <= 18:
    if day == "Monday":
        open = "open"
    elif day == "Tuesday":
        open = "open"
    elif day == "Wednesday":
        open = "open"
    elif day == "Thursday":
        open = "open"
    elif day == "Friday":
        open = "open"
    elif day == "Saturday":
        open = "open"
    else:
        open = "closed"
else:
    open = "closed"
print(open)
