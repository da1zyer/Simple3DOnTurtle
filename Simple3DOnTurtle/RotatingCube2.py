import turtle

t = turtle.Turtle()
t.hideturtle()
t.speed(100)


def displace(offset):
    t.forward(offset*1.2)
    t.left(90)
    t.forward(offset*1.15)
    t.right(90)


def right_face(side, angle, offset):
    t.left(angle + offset)
    t.forward(side)
    t.left(90 - angle - offset)
    t.forward(side)
    t.left(90 + angle + offset)
    t.forward(side)
    t.left(90 - angle - offset)
    t.forward(side)


def left_face(side, angle, offset):
    t.right(angle - offset)
    t.forward(side)
    t.right(90 - angle + offset)
    t.forward(side)
    t.right(90 + angle - offset)
    t.forward(side)
    t.right(90 - angle + offset)
    t.forward(side)


def draw(side, angle, step):
    for offset in range(0, 90, step):
        t.penup()
        displace(offset)
        t.pendown()
        right_face(side, angle, offset)
        t.right(90)
        left_face(side, angle, offset)
        t.right(90 + angle - offset)
        t.forward(side)
        t.right(180 - angle + offset)
        right_face(side, angle, offset)
        t.penup()
        t.home()
        displace(offset)
        t.pendown()
        t.left(angle + offset)
        t.forward(side)
        t.left(90 - angle - offset)
        t.left(90)
        left_face(side, angle, offset)
        t.penup()
        t.home()
        t.pendown()
        t.clear()


while True:
    draw(150, 45, 10)
