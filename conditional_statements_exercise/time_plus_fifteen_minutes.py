hours = int(input())
minutes = int(input())

sum_minutes = hours * 60 + minutes + 15

total_hours = sum_minutes // 60
total_minutes = sum_minutes % 60

if total_hours > 23:
    total_hours = 0

if total_minutes < 10:
    print (f"{total_hours}:0{total_minutes}")
else:
    print(f"{total_hours}:{total_minutes}")