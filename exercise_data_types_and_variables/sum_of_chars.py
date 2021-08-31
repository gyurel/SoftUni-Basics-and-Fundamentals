n = int(input())

total = 0

for _ in range(n):
    current = input()
    current = ord(current)
    total += current

print(f"The sum equals: {total}")
