countries_list = input().split(", ")
capitals_list = input().split(", ")

country_capitals_dict = dict(zip(countries_list, capitals_list))

for country, capital in country_capitals_dict.items():
    print(f"{country} -> {capital}")

# print(f"{country} -> {capital}" for country, capital in country_capitals_dict.items())
