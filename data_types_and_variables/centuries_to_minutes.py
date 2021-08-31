centuries = int(input())

# 1 centuries = 100 years = 36524 days = 876576 hours = 52594560 minutes / 365.2422

years = centuries * 100
days = int(years * 365.2422)
hours = days * 24
minutes = hours * 60

print(f"{centuries} centuries = {years} years = {round(days)} days = {hours} hours = {minutes} minutes")
