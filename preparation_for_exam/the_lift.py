waiting_people = int(input())

wagons_occupation = [int(el) for el in input().split()]


for i in range(len(wagons_occupation)):

    difference = 4 - wagons_occupation[i]

    if waiting_people < difference:
        difference = waiting_people

    wagons_occupation[i] += difference
    waiting_people -= difference
    if waiting_people == 0:
        break

if sum(wagons_occupation) % 4 != 0 and waiting_people == 0:
    print(f"The lift has empty spots!\n{' '.join(str(el) for el in wagons_occupation)}")

elif sum(wagons_occupation) % 4 == 0 and waiting_people > 0:
    print(f"There isn't enough space! {waiting_people} people in a queue!\n{' '.join(str(el) for el in wagons_occupation)}")

elif sum(wagons_occupation) % 4 == 0 and waiting_people == 0:
    print(f"{' '.join(str(el) for el in wagons_occupation)}")
