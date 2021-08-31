def next_version(version_string):

    new_version_int = int("".join(version_string))
    new_version_int += 1
    new_version_str = str(new_version_int)
    new_version_list = [el for el in new_version_str]
    print_version_str = ".".join(new_version_list)

    return print_version_str


version_string = input().split(" ")

print(next_version(version_string))
