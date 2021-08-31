input_string = input()

users_register = {}

while not input_string == "Lumpawaroo":

    if " | " in input_string:

        command = input_string.split(" | ")
        force_side = command[0]
        force_user = command[1]

        if not force_side in users_register:
            users_register[force_side] = []

        force_user_in_users = False

        for users in users_register.values():
            if force_user in users:
                force_user_in_users = True

        if force_user_in_users:
            input_string = input()
            continue
        else:
            users_register[force_side].append(force_user)

    elif " -> " in input_string:

        command = input_string.split(" -> ")
        force_user = command[0]
        force_side = command[1]
        user_not_in_values = True

        for key_side, key_val_list in users_register.items():
            if force_user in key_val_list:
                users_register[key_side].remove(force_user)
                users_register[force_side].append(force_user)
                user_not_in_values = False

        if user_not_in_values and force_side in users_register:
            users_register[force_side].append(force_user)

        elif user_not_in_values and not force_side in users_register:
            users_register[force_side] = [force_user]

        print(f"{force_user} joins the {force_side} side!" )

    input_string = input()

for (key_force_side, key_force_users) in sorted(users_register.items(), key= lambda kvp:(-(len(kvp[1])), kvp[0])):
    if len(key_force_users) == 0:
        continue
    else:
        print(f"Side: {key_force_side}, Members: {len(key_force_users)}")
    for user in sorted(key_force_users):
        print(f"! {user}")
