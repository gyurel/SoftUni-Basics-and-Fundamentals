kvp = input()

stocks_dict = {}

while kvp != "statistics":
    kvp_list = kvp.split(": ")

    if kvp_list[0] in stocks_dict:
        stocks_dict[kvp_list[0]] += int(kvp_list[1])
    else:
        stocks_dict[kvp_list[0]] = int(kvp_list[1])

    kvp = input()

print("Products in stock:")
for key, value in stocks_dict.items():
    print(f"- {key}: {value}")
print(f"Total Products: {len(stocks_dict)}")
print(f"Total Quantity: {sum(stocks_dict.values())}")
