followers = {}

command_line = input()

while command_line != "Log out":

    command = command_line.split(": ")

    if "New follower" in command_line:

        name = command[1]
        if name not in followers:
            followers[name] = {'likes': 0, 'comments': 0}

    elif "Like" in command_line:
        name = command[1]
        count = int(command[2])

        if name not in followers:
            followers[name] = {'likes': count, 'comments': 0}
        else:
            followers[name]['likes'] += count

    elif "Comment" in command_line:
        user = command[1]

        if user not in followers:
            followers[user] = {'likes': 0, 'comments': 1}
        else:
            followers[user]['comments'] += 1

    elif "Blocked" in command_line:
        user = command[1]
        if user not in followers:
            print(f"{user} doesn't exist.")
        else:
            del followers[user]

    command_line = input()

new_followers_dict = {}

for key, val in followers.items():
    total = val['likes'] + val['comments']
    new_followers_dict[key] = total
#
# print(new_followers_dict)
new_followers_dict_sorted = {name: val for name, val in sorted(new_followers_dict.items(), key=lambda x: (-x[1], x[0]))}

# print(new_followers_dict_sorted)

print(f"{len(new_followers_dict_sorted)} followers")
for person, likecomments in new_followers_dict_sorted.items():
    print(f"{person}: {likecomments}")
