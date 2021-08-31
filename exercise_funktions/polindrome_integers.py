def check_polindrome(check_str):
    check_list = check_str.split(", ")

    result_list = []
    for element in check_list:
        concurrent_element = element[::-1]
        if concurrent_element == element:
            result_list.append("True")
        else:
            result_list.append("False")

    return result_list


check_str = input()

for element in check_polindrome(check_str):
    print(element)
