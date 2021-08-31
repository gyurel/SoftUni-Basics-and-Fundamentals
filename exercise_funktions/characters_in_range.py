def get_char(char1, char2):

    list_of_characters = []
    for char in range(ord(char1) + 1, ord(char2)):
        concurrent_char = chr(char)
        list_of_characters.append(concurrent_char)

    return list_of_characters


char1 = input()
char2 = input()

for element in get_char(char1, char2):
    print(f"{element}", end=" ")
