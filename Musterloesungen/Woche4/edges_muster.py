import stddraw
from math import sqrt

def draw_img(img : 'list[list[int]]'):
    for y in range(len(img)):
        for x in range(len(img[y])):
            height = len(img)
            width = len(img[y])
            stddraw.setPenColor(stddraw.color.Color(int(img[y][x]), int(img[y][x]), int(img[y][x])))
            stddraw.rectangle(x / width,1 - y / height, 1 / width, 1 / height)
    stddraw.show()

# ---- a ----
img = []
with open('image.raw', 'r') as f:
    for line in f:
        img.append(list(map(int, line.strip().split())))        

# ---- b ----

nabla_img = []
max_grad = 0
for y in range(len(img)):
    line = []
    nabla_img.append(line)
    for x in range(len(img[y])):
        # check if you are at the edge
        if x == len(img[y]) - 1 or y == len(img) - 1:
            line.append(0)
        else:
            # use formula from the sheet
            grad = sqrt((img[y][x+1] - img[y][x])**2 + (img[y+1][x] - img[y][x])**2)
            max_grad = max(max_grad, grad)  # for c
            line.append(grad)

# ---- c ----

for y in range(len(nabla_img)):
    for x in range(len(nabla_img[y])):
        if nabla_img[y][x] > max_grad * 0.33:
            nabla_img[y][x] = 255
        else:
            nabla_img[y][x] = 0

draw_img(nabla_img)
