goal = 10000
steps_so_far = 0
goal_reached = True

while steps_so_far < goal:
    command = input()
    if command == "Going home":
        steps_to_home = int(input())
        steps_so_far += steps_to_home
        if steps_so_far < goal:
            goal_reached = False
            break
        else:
            break
    steps_so_far += int(command)

if goal_reached:
    print(f"Goal reached! Good job!")
    print(f"{steps_so_far - goal} steps over the goal!")
else:
    print(f"{goal - steps_so_far} more steps to reach goal.")
