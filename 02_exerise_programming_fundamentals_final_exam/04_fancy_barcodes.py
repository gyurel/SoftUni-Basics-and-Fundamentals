import re

pattern = r"^(@[#]+)(?P<barcode>[A-Z][A-Za-z0-9]{4,}[A-Z])(@[#]+)$"

n = int(input())


for i in range(n):
    input_string = input()

    match = re.match(pattern, input_string)

    if match == None:
        print("Invalid barcode")

    else:
        group = ""
        current_group = ""
        barcode = match.group('barcode')
        for chr in barcode:
            if chr.isdigit():
                current_group += chr
        if current_group != "":
            group = current_group
        else:
            group = "00"


        print(f"Product group: {group}")
