#26.00 - 35.00	Hot
#20.1 - 25.9	Warm
#15.00 - 20.00	Mild
#12.00 - 14.9	Cool
#5.00 - 11.9	Cold

temperature = float(input())

if 26.00 <= temperature <= 35.00:
    print("Hot")
elif 20.1 <= temperature <= 25.9:
    print("Warm")
elif 15.00 <= temperature <= 20.00:
    print("Mild")
elif 12.00 <= temperature <= 14.9:
    print("Cool")
elif 5.00 <= temperature <= 11.9:
    print("Cold")
else:
    print("unknown")