n = int(input())
word = input()

whole_list = []
including_list = []

for _ in range(n):
    some_string = input()
    whole_list.append(some_string)
    if word in some_string:
        including_list.append(some_string)

print(whole_list)
print(including_list)
