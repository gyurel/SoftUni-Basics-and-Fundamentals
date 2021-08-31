def word_filter(words_string):

    even_list = [el for el in words_string if len(el) % 2 == 0]

    return even_list


word_string = input().split(" ")
a = word_filter(word_string)

for el in a:
    print(el)
