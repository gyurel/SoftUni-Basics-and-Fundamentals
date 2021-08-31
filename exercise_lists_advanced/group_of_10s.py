def group_digits(input_sequence):

    sequence_list = [int(el) for el in input_sequence]
    print_list = []
    group = 10

    while sequence_list:
        group_list = [el for el in sequence_list if el <= group]
        for el in group_list:
            sequence_list.remove(el)
        print_list.append(f"Group of {group}'s: {group_list}")
        group += 10
        group_list = []

    return print_list

input_sequence = input().split(", ")
for el in group_digits(input_sequence):
    print(el)
