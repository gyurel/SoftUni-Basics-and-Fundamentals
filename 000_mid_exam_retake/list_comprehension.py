from itertools import product

x = int(input())
y = int(input())
z = int(input())
n = int(input())

parameters = [x, y, z]

full_parameters = [[i for i in range(el + 1)] for el in parameters]

possible_coordinates = [list(P) for P in product(*full_parameters) if sum(P) != n]

print(possible_coordinates)
