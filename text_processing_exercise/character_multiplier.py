input_string = input().split()

total = 0
there_is_a_rest = True

word_1 = input_string[0]
word_2 = input_string[1]

shorter_word = min(len(word_1), len(word_2))
longer_word = max(len(word_1), len(word_2))

for i in range(shorter_word):
    first_number = ord(word_1[i])
    second_number = ord(word_2[i])
    current_product = first_number * second_number
    total += current_product

rest_part = ""
if len(word_1) > len(word_2):
    rest_part = word_1[shorter_word:]
elif len(word_1) < len(word_2):
    rest_part = word_2[shorter_word:]
else:
    there_is_a_rest = False


if there_is_a_rest:
    for i in range(len(rest_part)):
        char = ord(rest_part[i])
        total += char

print(total)
