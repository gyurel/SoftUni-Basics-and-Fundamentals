# def shoot_target(index, power):
#     if 0 <= index <= len(target_sequence) - 1:
#         new_value = int(target_sequence[index]) - power
#         if new_value > 0:
#             target_sequence.pop(index)
#             target_sequence.insert(index, str(new_value))
#         else:
#             target_sequence.pop(index)
#     else:
#         pass
#
#     return target_sequence
#
#
# def add_target(index, value):
#     if 0 <= index <= len(target_sequence) - 1:
#         target_sequence.insert(index, value)
#         return target_sequence
#     else:
#         return f"Invalid placement!"


def strike(index, radius):
    left_border = index - radius
    right_border = index + radius
    if 0 <= left_border <= len(target_sequence) - 1 and 0 <= right_border <= len(target_sequence) - 1:
        remove_list = []
        for i in range(left_border, right_border + 1):
            remove_list.append(target_sequence[i])
        for str in remove_list:
            target_sequence.remove(str)
        return target_sequence
    else:
        return "Strike missed!"


target_sequence = input().split()

command = input().split()
index = int(command[1])
radius = int(command[2])
strike(index, radius)
