products = input().split()

stocs = {}

for index in range(0, len(products), 2):
    key = products[index]
    value = products[index + 1]
    stocs[key] = int(value)

print(stocs)
