exam_hour = int(input()) * 60
exam_minutes = int(input())
coming_hour = int(input()) * 60
coming_minutes = int(input())

exam_time = exam_hour + exam_minutes
coming_time = coming_hour + coming_minutes
time_calculation = exam_time - coming_time

if 0 <= time_calculation <= 30:
    print("On time")
elif time_calculation < 0:
    print("Late")
elif time_calculation > 30:
    print("Early")

if 1 <= time_calculation <= 59:
    print(f"{time_calculation} minutes before the start")
elif time_calculation >= 60:
    difference_hour = time_calculation // 60
    difference_minute = time_calculation % 60
    if difference_minute < 10:
        print(f"{difference_hour}:0{difference_minute} hours before the start")
    else:
        print(f"{difference_hour}:{difference_minute} hours before the start")
elif -1 >= time_calculation > -60:
        print(f"{abs(time_calculation)} minutes after the start")
elif time_calculation <= -60:
    difference_hour = abs(time_calculation) // 60
    difference_minute = abs(time_calculation) % 60
    if difference_minute < 10:
        print(f"{difference_hour}:0{difference_minute} hours after the start")
    else:
        print(f"{difference_hour}:{difference_minute} hours after the start")
else:
    print("")
