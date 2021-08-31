import math

length = float(input()) * 100

width = (float(input()) * 100) - 100

desks_per_row = math.floor(width / 70)
total_rows = math.floor(length / 120)

total_desks = (desks_per_row * total_rows) - 3

print(total_desks)
