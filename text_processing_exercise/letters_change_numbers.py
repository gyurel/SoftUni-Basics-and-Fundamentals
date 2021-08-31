input_str = input().split()

alphabet_lowercase = 'abcdefghijklmnopqrstuvwxyz'
alphabet_uppercase = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
total = 0

for el in input_str:
    first_letter = el[:1]
    number = int(el[1:-1])
    second_letter = el[-1:]

    if first_letter.isupper():
        position = alphabet_uppercase.index(first_letter) + 1
        total += number / position
    else:
        position = alphabet_lowercase.index(first_letter) + 1
        total += number * position

    if second_letter.isupper():
        position = alphabet_uppercase.index(second_letter) + 1
        total -= position
    else:
        position = alphabet_lowercase.index(second_letter) + 1
        total += position


print(f"{total:.2f}")
