#Да се напише програма, в която потребителят въвежда вида и размерите на геометрична фигура и пресмята лицето й.
# Фигурите са четири вида: квадрат (square), правоъгълник (rectangle), кръг (circle) и триъгълник (triangle).
# На първия ред на входа се чете вида на фигурата (square, rectangle, circle или triangle):

import math
type_of_figure = input()

#•	Ако фигурата е квадрат, на следващия ред се чете едно число - дължина на страната му;

if type_of_figure == "square":
    side = float(input())
    square_area = side * side
    print(f"{square_area:.3f}")

#•	Ако фигурата е правоъгълник, на следващите два реда четат две числа - дължините на страните му;

elif type_of_figure == "rectangle":
    side_a = float(input())
    side_b = float(input())
    area_rectangel = side_a * side_b
    print(f"{area_rectangel:.3f}")

#•	Ако фигурата е кръг, на следващия ред чете едно число - радиусът на кръга;

elif type_of_figure == "circle":
    radius = float(input())
    circle_area = math.pi * radius * radius
    print(f"{circle_area:.3f}")

#•	Ако фигурата е триъгълник, на следващите два реда четат две числа
# - дължината на страната му и дължината на височината към нея.

elif type_of_figure == "triangle":
    side_triangle = float(input())
    height_triangle = float(input())
    area_triangle = side_triangle * height_triangle / 2
    print(f"{area_triangle:.3f}")

#Резултатът да се закръгли до 3 цифри след десетичната точка.
