initial_username = input()

cmd = input()

while cmd != "Registration":

    cmd = cmd.split()

    if "Letters" in cmd:
        command = cmd[1]

        if command == "Lower":
            initial_username = initial_username.lower()
            print(initial_username)
        elif command == "Upper":
            initial_username = initial_username.upper()
            print(initial_username)

    elif "Reverse" in cmd:
        start_index = int(cmd[1])
        end_index = int(cmd[2])

        if 0 <= start_index <= len(initial_username) - 1 and 0 <= end_index <= len(initial_username) - 1:
            substring = initial_username[start_index:end_index + 1]
            substring = substring[::-1]
            print(substring)

    elif "Substring" in cmd:
        substr = cmd[1]

        if substr in initial_username:
            initial_username = initial_username.replace(substr, "")
            print(initial_username)
        else:
            print(f"The username {initial_username} doesn't contain {substr}.")

    elif "Replace" in cmd:
        replace_char = cmd[1]

        initial_username = initial_username.replace(replace_char, "-")
        print(initial_username)

    elif "IsValid" in cmd:
        char = cmd[1]
        if char in initial_username:
            print(f"Valid username.")
        else:
            print(f"{char} must be contained in your username.")

    cmd = input()

exit(0)