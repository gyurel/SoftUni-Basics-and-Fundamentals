conceild_message = input()

cmd = input()

while cmd != "Reveal":

    command = cmd.split(":|:")

    if "InsertSpace" in command:
        index = int(command[1])
        first_part = conceild_message[0:index]
        last_part = conceild_message[index:]
        conceild_message = first_part + " " + last_part
        print(conceild_message)

    elif "Reverse" in command:
        substring = command[1]
        substring_reversed = substring[::-1]
        if substring in conceild_message:
            conceild_message = conceild_message.replace(substring, "", 1)
            conceild_message += substring_reversed
            print(conceild_message)
        else:
            print("error")

    elif "ChangeAll" in command:
        substring = command[1]
        replacement = command[2]
        conceild_message = conceild_message.replace(substring, replacement)
        print(conceild_message)

    cmd = input()

print(f"You have a new text message: {conceild_message}")
