destination = input()


while destination != "End":
    budget = float(input())
    collected_sum = 0
    while collected_sum < budget:
        new_sum = float(input())
        collected_sum += new_sum

    else:
        print(f"Going to {destination}!")

    destination = input()
