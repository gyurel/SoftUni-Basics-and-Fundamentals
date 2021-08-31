# Иван решава да подобри Световния рекорд по плуване на дълги разстояния. На конзолата се въвежда рекордът
# в секунди, който Иван трябва да подобри,  разстоянието в метри, което трябва да преплува и времето в секунди,
# за което плува разстояние от 1 м. Да се напише програма, която изчислява дали се е справил със задачата,
# като се има предвид, че: съпротивлението на водата го забавя на всеки 15 м. с 12.5 секунди. Когато се изчислява
# колко пъти Иванчо ще се забави, в резултат на съпротивлението на водата, резултатът трябва да се закръгли надолу
# до най-близкото цяло число.
# Да се изчисли времето в секунди, за което Иванчо ще преплува разстоянието и разликата спрямо Световния рекорд.

record_seconds = float(input())
distance_meters = float(input())
time_seconds_one_meter = float(input())

latenance_in_seconds = (distance_meters // 15) * 12.5

result_seconds = distance_meters * time_seconds_one_meter + latenance_in_seconds

if result_seconds < record_seconds:
    print(f" Yes, he succeeded! The new world record is {result_seconds:.2f} seconds.")
else:
    needed_time_seconds = result_seconds - record_seconds
    print(f"No, he failed! He was {needed_time_seconds:.2f} seconds slower.")