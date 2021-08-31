# •	K - началото на интервала за първото число от първия номер – цяло число в интервала [0..8]
# •	L - началото на интервала за второто число от първия номер – цяло число в интервала [9..0]
# •	M - началото на интервала за първото число от втория номер – цяло число в интервала [0..8]
# •	N - началото на интервала за второто число от втория номер – цяло число в интервала [9..0]

num1_dig1 = int(input())
num1_dig2 = int(input())
num2_dig1 = int(input())
num2_dig2 = int(input())

counter = 0

for dig1_num1 in range(num1_dig1, 9):
    if counter == 6:
        break
    for dig2_num1 in range(9, num1_dig2-1, -1):
        if counter == 6:
            break
        num1 = int(str(dig1_num1) + str(dig2_num1))
        for dig1_num2 in range(num2_dig1, 9):
            if counter == 6:
                break
            for dig2_num2 in range(9, num2_dig2-1, -1):
                num2 = int(str(dig1_num2) + str(dig2_num2))
                if dig1_num1 % 2 == 0 and dig2_num1 % 2 == 1 and dig1_num2 % 2 == 0 and dig2_num2 % 2 == 1 and num1 != num2:
                    print(f"{dig1_num1}{dig2_num1} - {dig1_num2}{dig2_num2}")
                    counter += 1
                elif dig1_num1 % 2 == 0 and dig2_num1 % 2 == 1 and dig1_num2 % 2 == 0 and dig2_num2 % 2 == 1 and num1 == num2:
                    print("Cannot change the same player.")
                if counter == 6:
                    break
# На конзолата да се отпечатат първите 6 възможни смени по следния начин:
# •	Ако смяната е възможна и номерата НЕ съвпадат, да се отпечата:
# "{K}{L} - {M}{N}"
# •	Ако смяната е възможна и номерата съвпадат, да се отпечата:
# "Cannot change the same player."