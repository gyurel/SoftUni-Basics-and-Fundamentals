# •	K - началото на интервала за първото число от първия номер – цяло число в интервала [0..8]
# •	L - началото на интервала за второто число от първия номер – цяло число в интервала [9..0]
# •	M - началото на интервала за първото число от втория номер – цяло число в интервала [0..8]
# •	N - началото на интервала за второто число от втория номер – цяло число в интервала [9..0]

k = int(input())
l = int(input())
m = int(input())
n = int(input())

counter = 0

for dig1_aa in range(k, 9):
    if counter == 6:
        break
    for dig2_aa in range(9, l-1, -1):
        if counter == 6:
            break
        aa = int(str(dig1_aa) + str(dig2_aa))

        for dig1_bb in range(m, 9):
            if counter == 6:
                break
            for dig2_bb in range(9, n-1, -1):
                bb = int(str(dig1_bb) + str(dig2_bb))
                if dig1_aa % 2 == 0 and dig2_aa % 2 == 1 and dig1_bb % 2 == 0 and dig2_bb % 2 == 1 and aa != bb:
                    print(f"{dig1_aa}{dig2_aa} - {dig1_bb}{dig2_bb}")
                    counter += 1
                elif dig1_aa % 2 == 0 and dig2_aa % 2 == 1 and dig1_bb % 2 == 0 and dig2_bb % 2 == 1 and aa == bb:
                    print("Cannot change the same player.")
                if counter == 6:
                    break
# На конзолата да се отпечатат първите 6 възможни смени по следния начин:
# •	Ако смяната е възможна и номерата НЕ съвпадат, да се отпечата:
# "{K}{L} - {M}{N}"
# •	Ако смяната е възможна и номерата съвпадат, да се отпечата:
# "Cannot change the same player."