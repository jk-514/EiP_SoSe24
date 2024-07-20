import stddraw

MAX = 2.1
W = 720
H = 480
stddraw.setCanvasSize(W,H)


def mandelbrot(c, i):
    if i == 0:
        return 0
    r = mandelbrot(c, i-1)**2 + c 
    if abs(r) > MAX:
        return MAX
    else:
        return r
    
def show_mandelbrot(n,ms = float('inf')):
    stddraw.setXscale(-2,1)
    stddraw.setYscale(-1, 1)
    stddraw.setPenRadius(0.002)
    
    for x in range(-2*W//3, W//3+1):
        for y in range(-H//2, H//2+1):
            c = complex(x/(W//3), y/(H//2))
            z = mandelbrot(c, n)
            if abs(z) < MAX:
                stddraw.point(c.real, c.imag)
    stddraw.show(ms)



for n in range(1, 20):
    show_mandelbrot(n, 33)
    stddraw.clear()

show_mandelbrot(100)
