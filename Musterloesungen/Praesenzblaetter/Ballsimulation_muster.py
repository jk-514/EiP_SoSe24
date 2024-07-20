import stddraw as draw

draw.setPenColor(draw.RED)
draw.setPenRadius(0.001)
x = 0.5
y = 0.5
v_x = 0.0
v_y = 0.0
masse = 100
G = 0
mouse_x = -1
mouse_y = -1
while True:
    # a) ------------
    if draw.mousePressed():
        mouse_x = draw.mouseX()
        mouse_y = draw.mouseY()
        # start the program once mouse pressed
        G = 9.81
    # ---------------
    
    # b) ------------
    a_x = 0
    a_y = 0
    if mouse_x != -1:
        a_x = (mouse_x - x) / masse
        a_y = (mouse_y - y) / masse
    # ---------------

    # d) ------------
    a_y -= G / masse / 100 # scale G
    # ---------------

    # b) ------------
    v_x += a_x
    v_y += a_y
    # ---------------
    
    x += v_x
    y += v_y

    # c) -------
    v_x *= 0.98
    v_y *= 0.98
    # ----------

    # a) ------------
    if mouse_x != -1:
        draw.setPenColor(draw.BLACK)
        draw.line(x, y, mouse_x, mouse_y)
    # ---------------
    
    draw.setPenColor(draw.RED)
    draw.filledCircle(x, y, 0.02)
    draw.show(33)
    draw.clear()
