import re

pattern = r"([@#])(?P<word_one>[A-Za-z]{3,})(\1)(\1)(?P<word_two>[A-Za-z]{3,})(\1)"

matches_list = []
match_counter = 0

input_string = input()

match_words = re.finditer(pattern, input_string)
no_match_found = True


for match in match_words:
    no_match_found = False
    match_counter += 1
    word_one = match.group('word_one')
    word_two = match.group('word_two')
    word_two_reversed = word_two[::-1]
    if word_one == word_two_reversed:

        current_match = (word_one, word_two)
        matches_list.append(current_match)

if no_match_found:
    print("No word pairs found!")
    print("No mirror words!")

elif len(matches_list) == 0:
    print(f"{match_counter} word pairs found!")
    print("No mirror words!")

else:

    print(f"{match_counter} word pairs found!")
    print("The mirror words are:")
    for i in range(len(matches_list)):
        current_el = matches_list[i]
        if i == len(matches_list) - 1:
            print(f"{current_el[0]} <=> {current_el[1]}", end="")
        else:
            print(f"{current_el[0]} <=> {current_el[1]}", end=", ")
