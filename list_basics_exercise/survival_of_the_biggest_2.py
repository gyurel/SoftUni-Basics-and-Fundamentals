input_string = input().split()
input_string = [int(el) for el in input_string]
n = int(input())

for i in range(n):
    input_string.remove(min(input_string))

input_string = [str(el) for el in input_string]
print(", ".join(input_string))
