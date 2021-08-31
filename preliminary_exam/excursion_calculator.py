# 1.	Първи ред – брой хора – цяло число в интервала [1 … 20]
# 2.	Втори ред – сезон – текст с възможности - "spring", "summer", "autumn" или "winter"

count_people = int(input())
season = input()
total_sum = 0

if count_people <= 5:
    if season == "spring":
        total_sum = count_people * 50
    elif season == "summer":
        total_sum = count_people * 48.5 * 0.85
    elif season == "autumn":
        total_sum = count_people * 60
    elif season == "winter":
        total_sum = count_people * 86 * 1.08
elif count_people > 5:
    if season == "spring":
        total_sum = count_people * 48
    elif season == "summer":
        total_sum = count_people * 45 * 0.85
    elif season == "autumn":
        total_sum = count_people * 49.5
    elif season == "winter":
        total_sum = count_people * 85 * 1.08

print(f"{total_sum:.2f} leva.")
