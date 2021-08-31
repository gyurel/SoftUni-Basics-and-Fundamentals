movie_name = input()

free_seats = 0
total_sold_tickets = 0
student_tickets = 0
standard_tickets = 0
kids_tickets = 0
currently_sold_tickets = 0
seats_counter = free_seats

while movie_name != "Finish":
    free_seats = int(input())
    seats_counter = free_seats
    sold_ticket = input()
    while seats_counter > 0 and sold_ticket != "End":
        if sold_ticket == "student":
            student_tickets += 1
            currently_sold_tickets += 1
            total_sold_tickets += 1
            seats_counter -= 1
        elif sold_ticket == "standard":
            standard_tickets += 1
            currently_sold_tickets += 1
            total_sold_tickets += 1
            seats_counter -= 1
        elif sold_ticket == "kid":
            kids_tickets += 1
            currently_sold_tickets += 1
            total_sold_tickets += 1
            seats_counter -= 1
        if seats_counter <= 0:
            percentage = currently_sold_tickets / free_seats * 100
            print(f"{movie_name} - {percentage:.2f}% full.")
            currently_sold_tickets = 0
            movie_name = input()
            if movie_name == "Finish":
                break
        sold_ticket = input()

    else:
        percentage = currently_sold_tickets / free_seats * 100
        print(f"{movie_name} - {percentage:.2f}% full.")
        currently_sold_tickets = 0
        movie_name = input()
else:
    print(f"Total tickets: {total_sold_tickets}")
    student_percentage = student_tickets / total_sold_tickets * 100
    print(f"{student_percentage:.2f}% student tickets.")
    standard_percentage = standard_tickets / total_sold_tickets * 100
    print(f"{standard_percentage:.2f}% standard tickets.")
    kids_percentage = kids_tickets / total_sold_tickets * 100
    print(f"{kids_percentage:.2f}% kids tickets.")
