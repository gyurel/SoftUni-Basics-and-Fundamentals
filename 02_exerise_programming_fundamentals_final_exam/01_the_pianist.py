n = int(input())

pieces_dict = {}

for i in range(n):
    pieces_info = input().split("|")

    name = pieces_info[0]
    composer = pieces_info[1]
    key = pieces_info[2]

    pieces_dict[name] = {'Composer': composer, 'Key': key}

command = input()
while command != "Stop":

    command = command.split("|")

    if "Add" in command:
        name = command[1]
        composer = command[2]
        key = command[3]

        if name in pieces_dict:
            print(f"{name} is already in the collection!")
        else:
            pieces_dict[name] = {'Composer': composer, 'Key': key}
            print(f"{name} by {composer} in {key} added to the collection!")

    elif "Remove" in command:
        name = command[1]
        if name in pieces_dict:
            del pieces_dict[name]
            print(f"Successfully removed {name}!")
        else:
            print(f"Invalid operation! {name} does not exist in the collection.")

    elif "ChangeKey" in command:
        name = command[1]
        new_key = command[2]
        if name in pieces_dict:
            pieces_dict[name]['Key'] = new_key
            print(f"Changed the key of {name} to {new_key}!")
        else:
            print(f"Invalid operation! {name} does not exist in the collection.")

    command = input()

sorte_pieces = sorted(pieces_dict.items(), key=lambda x: (x[0], x[1]['Composer']))
sorted_pieces_dict = {name:value for name, value in sorted(pieces_dict.items(), key=lambda x: (x[0], x[1]['Composer']))}

# for name, data in sorted_pieces_dict:
#     print(f"{name} -> Composer: {data['Composer']}, Key: {data['Key']}")


for name, data in sorted_pieces_dict.items():
    print(f"{name} -> Composer: {data['Composer']}, Key: {data['Key']}")

# print(pieces_dict)
# print(sorte_pieces)
# print(sorted_pieces_dict)
