# Да се напише конзолна програма, която прочита възраст (реално число) и пол ('m' или 'f'),
# въведени от потребителя, и отпечатва обръщение измежду следните:
# •	"Mr." – мъж (пол 'm') на 16 или повече години
# •	"Master" – момче (пол 'm') под 16 години
# •	"Ms." – жена (пол 'f') на 16 или повече години
# •	"Miss" – момиче (пол 'f') под 16 години

age = float(input())
sex = input()
personal_title = ""

if sex == "m":
    if age >= 16:
        personal_title = "Mr."
    else:
        personal_title = "Master"
elif sex == "f":
    if age >= 16:
        personal_title = "Ms."
    else:
        personal_title = "Miss"
print(personal_title)
