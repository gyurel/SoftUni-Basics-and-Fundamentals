# •	Символ 1: цифра от 1 до n;
# •	Символ 2: цифра от 1 до n;
# •	Символ 3: малка буква измежду първите l букви на латинската азбука;
# •	Символ 4: малка буква измежду първите l букви на латинската азбука;
# •	Символ 5: цифра от 1 до n, по-голяма от първите 2 цифри.
print("Generate passwords with two number parameters defined from you.")
print("Insert the first number:", end=" ")
n = int(input())
print("Insert the second number:", end=" ")
l = int(input())

alphabet = "abcdefghijklmnopqrstuvwxyz"

for character1 in range(1, n+1):
    for character2 in range(1, n+1):
        for character3 in alphabet[0: l]:
            for character4 in alphabet[0: l]:
                if character1 > character2:
                    for character5 in range(character1+1, n+1):
                        print(f"{character1}{character2}{character3}{character4}{character5}", end=" ")
                else:
                    for character5 in range(character2+1, n+1):
                        print(f"{character1}{character2}{character3}{character4}{character5}", end=" ")
input("")
