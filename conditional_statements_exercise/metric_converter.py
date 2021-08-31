# •	Първи ред: число за преобразуване - реално число;
# •	Втори ред: входна мерна единица – текст;
# •	Трети ред: изходна мерна единица (за резултата) – текст.

value = float(input())
type_of_input = str(input())
type_of_output = str(input())

if type_of_input == "m" and type_of_output == "cm":
    result = value * 100
    print(f"{result:.3f}")
elif type_of_input == "m" and type_of_output == "mm":
    result = value * 1000
    print(f"{result:.3f}")
elif type_of_input == "cm" and type_of_output == "m":
    result = value / 100
    print(f"{result:.3f}")
elif type_of_input == "cm" and type_of_output == "mm":
    result = value * 10
    print(f"{result:.3f}")
elif type_of_input == "mm" and type_of_output == "m":
    result = value / 1000
    print(f"{result:.3f}")
elif type_of_input == "mm" and type_of_output == "cm":
    result = value / 10
    print(f"{result:.3f}")
