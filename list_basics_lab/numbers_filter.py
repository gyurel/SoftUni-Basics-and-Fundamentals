n = int(input())

even = []
odd = []
negative = []
positive = []



for _ in range(n):
    _ = int(input())
    if _ % 2 == 0:
        even.append(_)
    if _ % 2 == 1:
        odd.append(_)
    if _ < 0:
        negative.append(_)
    if _ >= 0:
        positive.append(_)

command = input()

if command == "even":
    print(even)
elif command == "odd":
    print(odd)
elif command == "negative":
    print(negative)
elif command == "positive":
    print(positive)
