import math

ux, uy = 2, 0
ax, ay = 16, 6

# a

d_u = math.sqrt((ux - ax) ** 2 + (uy - ay) ** 2)
print("Der Abstand zur Uni beträgt", d_u)

# b

hx, hy = 18, 2
gx = gy = 12
d_h = math.sqrt((hx - ax) ** 2 + (hy - ay) ** 2)
d_g = math.sqrt((gx - ax) ** 2 + (gy - ay) ** 2)

if d_u <= d_h and d_u <= d_g:
    print("Der Fußweg zur Uni ist am kürzesten.")
elif d_h <= d_u and d_h <= d_g:
    print("Der Fußweg zum Höfchen ist am kürzesten.")
else:
    print("Der Fußweg zur Goethestraße ist am kürzesten.")

# c

# Fußweg

t_u = d_u

# Höfchen

d_hu = math.sqrt((hx - ux) ** 2 + (hy - uy) ** 2)
t_h = d_h + d_hu/2

# Goethestraße

d_gu = math.sqrt((gx - ux) ** 2 + (gy - uy) ** 2)
t_g = d_g + d_gu/3

if t_u <= t_h and t_u <= t_g:
    print("Der Fußweg zur Uni ist am kürzesten")
elif t_h <= t_u and t_h <= t_g:
    print("Der Weg über das Höfchen ist am kürzesten")
else:
    print("Der Weg über die Goethestraße ist am kürzesten")
