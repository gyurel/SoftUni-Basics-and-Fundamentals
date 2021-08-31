# 1.	Доход в лева - реално число в интервала [100.00…1500.00];
# 2.	Среден успех -  реално число в интервала [3.00…6.00];
# 3.	Минимална работна заплата – реално число в интервала [100.00…600.00].
import math

income = float(input())
degree = float(input())
minimal_wage = float(input())

social_scholarship = minimal_wage * 0.35
degree_scholarship = degree * 25

# •	Ако ученикът няма право да получава стипендия, се извежда:
# "You cannot get a scholarship!"
# •	Ако ученикът има право да получава само социална стипендия:
# "You get a Social scholarship {стойност на стипендия} BGN"
# •	Ако ученикът има право да получава само стипендия за отличен успех:
# "You get a scholarship for excellent results {стойност на стипендията} BGN"
# •	Ако ученикът има право да получава и двата типа стипендии, ще получи по-голямата
# по сума, а ако са равни ще получи тази за отличен успех.

if income > minimal_wage and degree < 5.5:
    print("You cannot get a scholarship!")
elif income <= minimal_wage and 4.5 <= degree < 5.5:
    print(f"You get a Social scholarship {math.floor(social_scholarship)} BGN")
elif income > minimal_wage and 5.50 <= degree:
    print(f"You get a scholarship for excellent results {math.floor(degree_scholarship)} BGN")
elif income <= minimal_wage and 5.5 <= degree:
    if social_scholarship > degree_scholarship:
        print(f"You get a Social scholarship {math.floor(social_scholarship)} BGN")
    elif social_scholarship < degree_scholarship:
        print(f"You get a scholarship for excellent results {math.floor(degree_scholarship)} BGN")
    elif social_scholarship == degree_scholarship:
        print(f"You get a scholarship for excellent results {math.floor(degree_scholarship)} BGN")