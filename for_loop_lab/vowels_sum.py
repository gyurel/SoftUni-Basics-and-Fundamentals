text = input()

sum_vovels = 0

for i in text:
    if i == "a":
        sum_vovels += 1
    elif i == "e":
        sum_vovels += 2
    elif i == "i":
        sum_vovels += 3
    elif i == "o":
        sum_vovels += 4
    elif i == "u":
        sum_vovels += 5

print(sum_vovels)
