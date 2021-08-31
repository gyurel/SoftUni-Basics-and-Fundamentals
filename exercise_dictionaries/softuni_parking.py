n = int(input())

parking_status = {}

for i in range(n):

    command_line = input().split()

    if len(command_line) == 3:

        command = command_line[0]
        user_name = command_line[1]
        reg_plate = command_line[2]

        if user_name in parking_status:
            print(f"ERROR: already registered with plate number {reg_plate}")
        else:
            parking_status[user_name] = reg_plate
            print(f"{user_name} registered {reg_plate} successfully")
    else:

        command = command_line[0]
        user_name = command_line[1]

        if user_name in parking_status:

            parking_status.pop(user_name)
            print(f"{user_name} unregistered successfully")

        else:
            print(f"ERROR: user {user_name} not found")

for key, val in parking_status.items():
    print(f"{key} => {val}")
