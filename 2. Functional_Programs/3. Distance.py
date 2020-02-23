"""
3. Write a program that takes two integer command-line
   arguments x and y and prints the Euclidean distance
   from the point (x, y) to the origin (0, 0).
   The formulae to calculate distance = sqrt(x*x + y*y). Use Math.power function
"""

from math import *
X = int(input("Enter x: "))
Y = int(input("Enter y: "))
distance = sqrt(X*X + Y*Y)
print("Euclidean Distance:", distance)
