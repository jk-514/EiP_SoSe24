import stddraw as draw


class Ball:
    def __init__(self) -> None:
        self.radius = 0.02
        self.x = 0.5
        self.y = 0.5
        self.vx = self.vy = 0
        self.ax = self.ay = 0
        self.mass = 100

    def show(self) -> None:
        draw.setPenColor(draw.RED)
        draw.filledCircle(self.x, self.y, 0.02)

    def update(self, mouse_x: int, mouse_y: int, g: float) -> None:
        self.ax = self.ay = 0
        if mouse_x != -1:
            self.ax = (mouse_x - self.x) / self.mass
            self.ay = (mouse_y - self.y) / self.mass

        self.apply_force(g)

        self.vx += self.ax
        self.vy += self.ay

        self.x += self.vx
        self.y += self.vy

        self.vx *= 0.98
        self.vy *= 0.98

    def apply_force(self, g: float):
        self.ay -= g / self.mass / 100


def main():
    ball = Ball()
    draw.setPenRadius(0.001)
    g = 0
    mouse_x = -1
    mouse_y = -1
    while True:
        if draw.mousePressed():
            mouse_x = draw.mouseX()
            mouse_y = draw.mouseY()
            g = 9.81

        ball.update(mouse_x, mouse_y, g)

        if mouse_x != -1:
            draw.setPenColor(draw.BLACK)
            draw.line(ball.x, ball.y, mouse_x, mouse_y)

        ball.show()
        draw.show(33)
        draw.clear()


if __name__ == '__main__':
    main()
