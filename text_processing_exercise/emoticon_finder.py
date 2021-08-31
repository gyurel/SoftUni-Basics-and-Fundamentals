input_string = input()

emoticons_list = []

for i in range(len(input_string)):
    if input_string[i] == ":" and input_string[i + 1] != " ":
        current_emoticon = input_string[i] + input_string[i +1]
        emoticons_list.append(current_emoticon)

print(*emoticons_list, sep= '\n')
