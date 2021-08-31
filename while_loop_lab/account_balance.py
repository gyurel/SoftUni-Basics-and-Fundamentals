payment = input()

total = 0

while payment != "NoMoreMoney":
    if float(payment) <= 0:
        print("Invalid operation!")
        break
    else:
        print(f"Increase: {float(payment):.2f}")
        total += float(payment)
        payment = input()

print(f"Total: {total:.2f}")
