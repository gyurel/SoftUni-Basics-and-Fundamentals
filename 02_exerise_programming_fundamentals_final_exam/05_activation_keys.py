raw_key = input()

cmd = input()
while cmd != "Generate":

    if "Contains" in cmd:
        command = cmd.split(">>>")
        substring = command[1]
        if substring in raw_key:
            print(f"{raw_key} contains {substring}")
        else:
            print("Substring not found!")

    elif "Flip" in cmd:
        command = cmd.split(">>>")
        to_do = command[1]
        start_index = int(command[2])
        end_index = int(command[3])

        first_part = raw_key[0:start_index]
        middel_part = raw_key[start_index:end_index]
        last_part = raw_key[end_index:]

        if to_do == "Upper":
            middel_part = middel_part.upper()
            raw_key = first_part + middel_part + last_part
            print(raw_key)
        elif to_do == "Lower":
            middel_part = middel_part.lower()
            raw_key = first_part + middel_part + last_part
            print(raw_key)

    elif "Slice" in cmd:
        command = cmd.split(">>>")
        start_index = int(command[1])
        end_index = int(command[2])

        first_part = raw_key[0:start_index]
        last_part = raw_key[end_index:]
        raw_key = first_part + last_part
        print(raw_key)

    cmd = input()

print(f"Your activation key is: {raw_key}")
