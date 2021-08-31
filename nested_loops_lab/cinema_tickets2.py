movie_name = input()

total_seats_sold = 0
student_seats_sold = 0
standard_seats_sold = 0
kid_seats_sold = 0


while movie_name != "Finish":
    total_free_seats = int(input())
    sold_ticket = input()
    current_seats_counter = 0
    while sold_ticket != "End":
        if sold_ticket == "student":
            total_seats_sold += 1
            student_seats_sold += 1
            current_seats_counter += 1
        elif sold_ticket == "standard":
            total_seats_sold += 1
            standard_seats_sold += 1
            current_seats_counter += 1
        elif sold_ticket == "kid":
            total_seats_sold += 1
            kid_seats_sold += 1
            current_seats_counter += 1
        if current_seats_counter < total_free_seats:
            sold_ticket = input()
        else:
            print(f"{movie_name} - {current_seats_counter / total_free_seats * 100:.2f}% full.")
            current_seats_counter = 0
            movie_name = input()
            break
    else:
        print(f"{movie_name} - {current_seats_counter / total_free_seats * 100:.2f}% full.")
        current_seats_counter = 0
        movie_name = input()
else:
    print(f"Total tickets: {total_seats_sold}")
    print(f"{student_seats_sold / total_seats_sold * 100:.2f}% student tickets.")
    print(f"{standard_seats_sold / total_seats_sold * 100:.2f}% standard tickets.")
    print(f"{kid_seats_sold / total_seats_sold * 100:.2f}% kids tickets.")
