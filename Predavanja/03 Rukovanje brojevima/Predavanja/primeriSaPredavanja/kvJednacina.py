# import math
from math import sqrt
a = eval(input("a:"))
b = eval(input("b:"))
c = eval(input("c:"))
r = sqrt(b ** 2 - 4*a*c)
x1 = (-b + r) / (2 * a)
x2 = (-b - r) / (2 * a)
print(x1)
print(x2)