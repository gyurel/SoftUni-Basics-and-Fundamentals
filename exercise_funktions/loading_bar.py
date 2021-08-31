def loading_bar(number):
    print_list = []

    bars = int(number % 100 / 10)
    print_string = ""
    empty_space = int(10 - bars)
    print_list.append("%" * bars)
    print_list.append("." * empty_space)

    for element in print_list:
        print_string += element

    return print(f"{number}% [{print_string}]\nStill loading..." if number < 100 else "100% Complete!\n[%%%%%%%%%%]" )

# if number < 100:
#     print(f"{number}% [{print_string}]")
#     print("Still loading...")
# else:
#     print("100% Complete!")
#     print("[%%%%%%%%%%]")

number = int(input())
loading_bar(number)
