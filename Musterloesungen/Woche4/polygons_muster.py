import stddraw
import math

polys_x = []
polys_y = []
max_p = [-math.inf]*2
min_p = [math.inf]*2
with open('map.txt', 'r') as f:
    for line in f:
        line = line.strip()
        if line == 'p:':
            poly_x = []
            polys_x.append(poly_x)
            poly_y = []
            polys_y.append(poly_y)
        else:
            x, y = line.split()
            poly_x.append(float(x))
            poly_y.append(float(y))
            max_p = [max(max_p[0], float(x)), max(max_p[1], float(y))]
            min_p = [min(min_p[0], float(x)), min(min_p[1], float(y))]

scale = max(max_p[0] - min_p[0], max_p[1] - min_p[1])

polys_x = [list(map(lambda x: 0.5 + (x - (max_p[0] + min_p[0]) / 2) / scale, poly_x)) for poly_x in polys_x]
polys_y = [list(map(lambda y: 0.5 + (y - (max_p[1] + min_p[1]) / 2) / scale, poly_y)) for poly_y in polys_y]

for poly_x, poly_y in zip(polys_x, polys_y):
    stddraw.polygon(poly_x, poly_y)

stddraw.show()
