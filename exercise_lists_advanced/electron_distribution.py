def electron_distribution(count_electrons):

    electrons_list = []
    current_layer = 0

    while count_electrons > 0:
        current_layer += 1
        current_layer_electron_count = 2 * current_layer ** 2
        if count_electrons >= current_layer_electron_count:
            electrons_list.append(current_layer_electron_count)
            count_electrons -= current_layer_electron_count
        else:
            electrons_list.append(count_electrons)
            break

    return electrons_list

count_electrons = int(input())
print(electron_distribution(count_electrons))
