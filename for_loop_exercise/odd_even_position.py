import sys
n = int(input())

# "OddSum=" + {сума на числата на нечетни позиции},
# "OddMin=" + { минимална стойност на числата на нечетни позиции } / {"No"},
# "OddMax=" + { максимална стойност на числата на нечетни позиции } / {"No"},
# "EvenSum=" + { сума на числата на четни позиции },
# "EvenMin=" + { минимална стойност на числата на четни позиции } / {"No"},
# "EvenMax=" + { максимална стойност на числата на четни позиции } / {"No"}

odd_sum = 0
odd_min = sys.maxsize
odd_max = -sys.maxsize
even_sum = 0
even_min = sys.maxsize
even_max = -sys.maxsize

for i in range(1, n+1):
    num = float(input())
    if i % 2 == 0:
        if num >= even_max:
            even_max = num
        if num <= even_min:
            even_min = num
        even_sum += num
    else:
        if num >= odd_max:
            odd_max = num
        if num <= odd_min:
            odd_min = num
        odd_sum += num

print(f"OddSum={odd_sum:.2f},")  # "OddSum=" + {сума на числата на нечетни позиции},
if odd_min == sys.maxsize:      # "OddMin=" + { минимална стойност на числата на нечетни позиции } / {"No"},
    print("OddMin=No,")
else:
    print(f"OddMin={odd_min:.2f},")

if odd_max == -sys.maxsize:     # "OddMax=" + { максимална стойност на числата на нечетни позиции } / {"No"},
    print("OddMax=No,")
else:
    print(f"OddMax={odd_max:.2f},")

print(f"EvenSum={even_sum:.2f},") # "EvenSum=" + { сума на числата на четни позиции },
if even_min == sys.maxsize:
    print("EvenMin=No,")                  # "EvenMin=" + { минимална стойност на числата на четни позиции } / {"No"},
else:
    print(f"EvenMin={even_min:.2f},")

if even_max == -sys.maxsize:     # "EvenMax=" + { максимална стойност на числата на четни позиции } / {"No"}
    print("EvenMax=No")
else:
    print(f"EvenMax={even_max:.2f}")
