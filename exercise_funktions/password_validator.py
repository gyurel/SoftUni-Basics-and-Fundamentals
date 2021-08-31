def validator(password_str):

    is_valid = True

    if 6 <= len(password_str) <= 10:
        pass
    else:
        print(f"Password must be between 6 and 10 characters")
        is_valid = False

    if password_str.isalnum():
        pass
    else:
        print(f"Password must consist only of letters and digits")
        is_valid = False

    digit_counter = 0
    for chr in password_str:
        if chr.isdigit() == True:
            digit_counter += 1
    if digit_counter > 1:
        pass
    else:
        is_valid = False
        print(f"Password must have at least 2 digits")

    if is_valid:
        print(f"Password is valid")


password_str = input()
validator(password_str)
