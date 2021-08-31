import re

pattern = r"^([\$|%])([A-Z][a-z]{2,})(\1)(:\s\[\d+\]\|\[\d+\]\|\[\d+\]\|$)"

n = int(input())

for i in range(n):

    input_str = input()

    message_groups = re.findall(pattern, input_str)
    if len(message_groups) == 0:
        print(f"Valid message not found!")

    message_groups = re.finditer(pattern, input_str)
    for match in message_groups:
        message = match.group()

        if message == "":
            print(f"Valid message not found!")
        else:
            raw_message = re.findall(pattern, input_str)
            numbers = re.findall("\d+", raw_message[0][3])
            decripted_mess = ""
            for el in numbers:
                ascii_code = int(el)
                char = chr(ascii_code)
                decripted_mess += char
            print(f"{raw_message[0][1]}: {decripted_mess}")

exit(0)
