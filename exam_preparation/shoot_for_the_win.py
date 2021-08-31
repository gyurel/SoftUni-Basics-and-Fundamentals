sequnce_str = [int(el) for el in input().split()]

command = input()
shot_count = 0

while command != "End":
    if 0 <= int(command) < len(sequnce_str):
        if sequnce_str[int(command)] != -1:
            operand = sequnce_str[int(command)]
            sequnce_str[int(command)] = -1
            for i in range(len(sequnce_str)):
                if i != int(command) and sequnce_str[i] != -1:
                    if sequnce_str[i] > operand:
                        sequnce_str[i] -= operand
                    else:
                        sequnce_str[i] += operand
            shot_count += 1
    command = input()

sequnce_str = [str(el) for el in sequnce_str]
print(f"Shot targets: {shot_count} -> {' '.join(sequnce_str)}")