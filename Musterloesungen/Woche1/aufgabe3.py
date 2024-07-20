import math

# a

a = float(input("a: "))
b = float(input("b: "))
c = float(input("c: "))

x1 = (-b + math.sqrt(b*b - 4*a*c)) / (2*a)
x2 = (-b - math.sqrt(b*b - 4*a*c)) / (2*a)

print(x1, x2)

# b

x_ext = -b/(2*a)

print(x_ext)
