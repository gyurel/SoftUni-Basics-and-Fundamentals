a = int(input())
b = int(input())

print("Before:")
print(f"a = {a}")
print(f"b = {b}")

c = a
d = b

a = d
b = c

print("After:")
print(f"a = {a}")
print(f"b = {b}")
