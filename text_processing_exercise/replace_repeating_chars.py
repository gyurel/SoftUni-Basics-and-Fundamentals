input_string = list(input())

copy_input_strin_list = input_string.copy()

result_string = ""
n = 0
done = False

while True:
    for i in range(n, len(input_string)):
        current_char = input_string[i]
        if i == len(input_string) - 1 and copy_input_strin_list[i] == " ":
            done = True
            break
        elif i == len(input_string) - 1:
            result_string += input_string[i]
            done = True
            break
        else:
            result_string += input_string[i]

            for j in range(i +1 , len(input_string)):
                if input_string[j] == input_string[i]:
                    copy_input_strin_list.pop(j)
                    copy_input_strin_list.insert(j, " ")
                    n = j
                else:
                    n = j
                    break

        break

    if done:
        break

print(result_string)
