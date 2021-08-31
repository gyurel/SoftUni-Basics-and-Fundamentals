password = input()

cmd = input()

while cmd != "Done":

    if "TakeOdd" in cmd:

        new_string = ""
        for i in range(len(password)):

            if i % 2 == 1:
                current_char = password[i]
                new_string += current_char
        password = new_string
        print(password)

    elif "Cut" in cmd:
        command = cmd.split()
        index = int(command[1])
        length = int(command[2])
        substring = password[index:index+length]
        new_string = password.replace(substring, "", 1)
        password = new_string
        print(password)

    elif "Substitute" in cmd:
        command = cmd.split()
        substr = command[1]
        substitute = command[2]
        if substr in password:
            new_str = password.replace(substr, substitute)
            password = new_str
            print(password)
        else:
            print("Nothing to replace!")

    cmd = input()

print(f"Your password is: {password}")
