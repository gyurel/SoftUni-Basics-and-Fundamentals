file_path = input().split("\\")

full_file_name = file_path[len(file_path) - 1]

splited_file_name = full_file_name.split(".")

file_name = splited_file_name[0]

file_extention = splited_file_name[1]

print(f"File name: {file_name}")
print(f"File extension: {file_extention}")
