width = int(input())
length = int(input())
total_peaces = width * length
eaten_pieces = 0
enough_peaces = True

while eaten_pieces <= total_peaces:
    command = input()
    if command == "STOP":
        if eaten_pieces > total_peaces:
            enough_peaces = False
            break
        else:
            break
    eaten_pieces += int(command)
else:
    enough_peaces = False


if enough_peaces:
    print(f"{total_peaces - eaten_pieces} pieces are left.")
else:
    print(f"No more cake left! You need {eaten_pieces - total_peaces} pieces more.")
