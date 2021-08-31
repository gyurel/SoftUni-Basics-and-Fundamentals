journey_price = float(input())
disposable_money = float(input())

count_days = 0
spending_days = 0

while disposable_money < journey_price and spending_days < 5:
    command = input()
    money = float(input())
    count_days += 1
    if command == "spend":
        spending_days += 1
        disposable_money -= money
        if disposable_money < 0:
            disposable_money = 0
    else:
        spending_days = 0
        disposable_money += money

if spending_days == 5:
    print("You can't save the money.")
    print(f"{count_days}")
elif disposable_money >= journey_price:
    print(f"You saved the money for {count_days} days.")
