# Град	    0 ≤ s ≤ 500	    500 < s ≤ 1 000	    1 000 < s ≤ 10 000	    s > 10 000
# Sofia	        5%	                7%	                8%	                12%
# Varna	        4.5%	            7.5%	            10%	                13%
# Plovdiv	    5.5%	            8%	                12%	                14.5%

town = input()
sales = float(input())
comission_rate = 0
comissio_sum = 0

if 0 <= sales <= 500:
    if town == "Sofia":
        comission_rate = 0.05
    elif town == "Varna":
        comission_rate = 0.045
    elif town == "Plovdiv":
        comission_rate = 0.055
    else:
        print("error")
elif 500 <= sales <= 1000:
    if town == "Sofia":
        comission_rate = 0.07
    elif town == "Varna":
        comission_rate = 0.075
    elif town == "Plovdiv":
        comission_rate = 0.08
    else:
        print("error")
elif 1000 <= sales <= 10000:
    if town == "Sofia":
        comission_rate = 0.08
    elif town == "Varna":
        comission_rate = 0.1
    elif town == "Plovdiv":
        comission_rate = 0.12
    else:
        print("error")
elif 10000 < sales:
    if town == "Sofia":
        comission_rate = 0.12
    elif town == "Varna":
        comission_rate = 0.13
    elif town == "Plovdiv":
        comission_rate = 0.145
    else:
        print("error")
else:
    print("error")

if comission_rate != 0:
    comissio_sum = sales * comission_rate
    print(f"{comissio_sum:.2f}")
