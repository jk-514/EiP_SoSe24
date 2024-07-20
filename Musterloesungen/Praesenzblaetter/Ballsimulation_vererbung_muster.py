import stddraw as draw
from abc import ABC, abstractmethod


class AnimatableObject(ABC):
    def __init__(self, x, y, vx, vy, ax, ay, mass):
        self.x = x
        self.y = y
        self.vx = vx
        self.vy = vy
        self.ax = ax
        self.ay = ay
        self.mass = mass

    def update(self):
        self.vx += self.ax
        self.vy += self.ay
        self.x += self.vx
        self.y += self.vy
        self.vx *= 0.98
        self.vy *= 0.98

    def apply_force(self, fx, fy):
        self.ax = fx / self.mass
        self.ay = fy / self.mass

    @abstractmethod
    def show(self):
        pass


class Ball(AnimatableObject):
    def __init__(self, x, y, radius, mass):
        super().__init__(x, y, 0, 0, 0, 0, mass)
        self.radius = radius

    def show(self):
        draw.setPenColor(draw.RED)
        draw.filledCircle(self.x, self.y, self.radius)


class Rectangle(AnimatableObject):
    def __init__(self, x, y, width, height, mass):
        super().__init__(x, y, 0, 0, 0, 0, mass)
        self.width = width
        self.height = height

    def show(self):
        draw.setPenColor(draw.RED)
        tlp_x = self.x - self.width/2
        tlp_y = self.y - self.height/2
        draw.filledRectangle(tlp_x, tlp_y, self.width, self.height)


draw.setPenColor(draw.RED)
draw.setPenRadius(0.001)

ball = Ball(0.5, 0.5, 0.02, 100)
# ball = Rectangle(0.5, 0.5, 0.2, 0.2, 100)

G = 0
mouse_x = -1
mouse_y = -1
while True:

    if draw.mousePressed():
        mouse_x = draw.mouseX()
        mouse_y = draw.mouseY()
        # start the program once mouse pressed
        G = 9.81
    
    f_x = 0
    f_y = 0
    if mouse_x != -1:
        f_x = (mouse_x - ball.x)
        f_y = (mouse_y - ball.y)

    f_y -= G / 100 # scale G

    ball.apply_force(f_x, f_y)
    
    ball.update()


    if mouse_x != -1:
        draw.setPenColor(draw.BLACK)
        draw.line(ball.x, ball.y, mouse_x, mouse_y)
    
    ball.show()

    draw.show(33)
    draw.clear()
