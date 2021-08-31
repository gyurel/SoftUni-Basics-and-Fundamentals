def perfect_number(number):
    list_of_devisors = []

# for devisor in range(1, number):
#     if number % devisor == 0:
#         list_of_devisors.append(devisor)
#
# if sum(list_of_devisors) == number:
#     print("We have a perfect number!")
# else:
#     print("It's not so perfect.")

    list_of_devisors = [devisor for devisor in range(1, number) if number % devisor == 0]
    return print("We have a perfect number!" if sum(list_of_devisors) == number else "It's not so perfect.")

# if sum(list_of_devisors) == number:
#     print("We have a perfect number!")
# else:
#     print("It's not so perfect.")
number = int(input())
perfect_number(number)
