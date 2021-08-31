encrypted_message = input()

command = input()

while command != "Decode":

    if "Move" in command:
        command = command.split("|")
        to_do = command[0]
        number_of_letters = int(command[1])

        first_part = encrypted_message[0:number_of_letters]
        second_part = encrypted_message[number_of_letters:]
        encrypted_message = second_part + first_part

    elif "Insert" in command:
        command = command.split("|")
        index = int(command[1])
        value = command[2]

        first_part = encrypted_message[0:index]
        second_part = encrypted_message[index:]
        encrypted_message = first_part + value + second_part

    elif "ChangeAll" in command:
        command = command.split("|")
        substring = command[1]
        replacement = command[2]

        encrypted_message = encrypted_message.replace(substring, replacement)

    command = input()

print(f"The decrypted message is: {encrypted_message}")
