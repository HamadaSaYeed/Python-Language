# python program to solve Quadratic Equation -- >> الثانيه االدرجه معادله حل


# solve the quadratic equation -- >>  ax**2 + bx + c = 0   << --

# import complex math module

import cmath

a = 1
b = 5
c = 6


# calculate the discriminant

d = (b**2) - (4*a*c) # 1



# find two solutions

sol1 = (-b-cmath.sqrt(d))/(2*a)
sol2 = (-b+cmath.sqrt(d))/(2*a)

print('the solution are {0} and {1}'.format(sol1,sol2)) # the solution are (-3+0j) and (-2+0j)