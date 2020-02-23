"""
4. Write a program Quadratic.java to find the roots of the equation a*x*x + b*x + c.
   Since the equation is x*x, hence there are 2 roots.
   The 2 roots of the equation can be found using a formula
   (Note: Take a, b and c as input values)
        delta = b*b - 4*a*c
        Root 1 of x = (-b + sqrt(delta))/(2*a)
        Root 2 of x = (-b - sqrt(delta))/(2*a)
"""

import cmath
a = float(input("Enter a: "))
b = float(input("Enter b: "))
c = float(input("Enter c: "))
if a != 0:
    d = (b**2)-(4*a*c)
    root1 = (-b-cmath.sqrt(d))/(2*a)
    root2 = (-b+cmath.sqrt(d))/(2*a)
    print(root1)
    print(root2)
