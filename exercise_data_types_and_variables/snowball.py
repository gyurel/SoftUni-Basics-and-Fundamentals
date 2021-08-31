n = int(input())

biggest_value_snow = 0
biggest_value_time = 0
biggest_value_quality = 0
biggest_snowball_value = 0

for i in range(n):
    snowball_snow = int(input())
    snowball_time = int(input())
    snowball_quality = int(input())
    snowball_value = (snowball_snow / snowball_time) ** snowball_quality
    if snowball_value > biggest_snowball_value:
        biggest_value_snow = snowball_snow
        biggest_value_time = snowball_time
        biggest_value_quality = snowball_quality
        biggest_snowball_value = snowball_value

print(f"{biggest_value_snow} : {biggest_value_time} = {int(biggest_snowball_value)} ({biggest_value_quality})")
