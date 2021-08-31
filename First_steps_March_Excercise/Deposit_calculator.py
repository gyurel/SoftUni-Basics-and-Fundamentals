deposit = float(input())
months = int(input())
interest_rate = float(input())/100

# сума = депозирана сума  + срок на депозита * ((депозирана сума * годишен лихвен процент ) / 12)

sum_lv = deposit + months * ((deposit * interest_rate)/12)

print(sum_lv)
