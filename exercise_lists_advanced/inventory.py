collecting_items = input().split(', ')

command = input()

while not command == 'Craft!':
    command = command.split(' - ')
    if command[0] == 'Collect':
        for item in collecting_items:
            if item == command[1]:
                continue
            else:
                collecting_items.append(command[1])
                break
    elif command[0] == 'Drop':
        for item in collecting_items:
            if item == command[1]:
                collecting_items.remove(item)
    elif command[0] == 'Combine Items':
        items = command[1].split(':')
        old_item = items[0]
        new_item = items[1]
        for index in range(len(collecting_items)):
            if collecting_items[index] == old_item:
                collecting_items.insert(index + 1, new_item)
    elif command[0] == 'Renew':
        for item in collecting_items:
            if item == command[1]:
                collecting_items.remove(item)
                collecting_items.append(item)
    command = input()

print(', '.join(collecting_items))
