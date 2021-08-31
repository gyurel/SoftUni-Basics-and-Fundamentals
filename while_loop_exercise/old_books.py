books_name = input()

count_books = 0


check_name = input()
while check_name != books_name and check_name != "No More Books":
    count_books += 1
    check_name = input()
else:
    if check_name == "No More Books":
        print("The book you search is not here!")
        print(f"You checked {count_books} books.")
    elif check_name == books_name:
        print(f"You checked {count_books} books and found it.")
