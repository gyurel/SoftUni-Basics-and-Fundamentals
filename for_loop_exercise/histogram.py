n = int(input())

p1 = 0
p2 = 0
p3 = 0
p4 = 0
p5 = 0

for i in range(1, n+1):
    num = int(input())
    if num < 200:
        p1 += 1
    if 200 <= num <= 399:
        p2 += 1
    if 400 <= num <= 599:
        p3 += 1
    if 600 <= num <= 799:
        p4 += 1
    if 800 <= num:
        p5 += 1

# p1 са под 200, друг процент p2 са от 200 до 399, друг процент p3 са от 400 до 599, друг процент p4 са от 600 до 799
# и останалите p5 процента са от 800 нагоре.

p1_percentage = (p1/n) * 100
p2_percentage = (p2/n) * 100
p3_percentage = (p3/n) * 100
p4_percentage = (p4/n) * 100
p5_percentage = (p5/n) * 100

print(f"{p1_percentage:.2f}%")
print(f"{p2_percentage:.2f}%")
print(f"{p3_percentage:.2f}%")
print(f"{p4_percentage:.2f}%")
print(f"{p5_percentage:.2f}%")
