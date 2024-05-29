# from sympy import symbols
poly_power = int(input("polynomial power: "));

coeffs = []
for i in range(poly_power):
    coef = float(input("Enter coffecient value for power: "))
    coeffs.append(coef)
poly_gradient = float(input("What is the gradient of the function? "))

f_of_x = 0
for i in range(poly_power):
    power = poly_power - i
    f_of_x += coeffs[i]