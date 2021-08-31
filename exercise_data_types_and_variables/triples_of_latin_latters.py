n = int(input())

for i in range(97, 97 + n):
    char1 = chr(i)
    for j in range(97, 97 + n):
        char2 = chr(j)
        for k in range(97, 97 + n):
            char3 = chr(k)
            print(char1 + char2 + char3)
