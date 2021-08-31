countries = input().split(", ")
capitals = input().split(", ")

# country_capital_dict = dict(zip(countries, capitals))
country_capital_tpl = zip(countries, capitals)

country_capital_dict = {key:val for key, val in country_capital_tpl}

for key, val in country_capital_dict.items():
    print(f"{key} -> {val}")
