import turtle

t = turtle.Turtle()
t.speed(500)


def square(side):
    for i in range(4):
        t.forward(side)
        t.right(90)


def edge(side, angle):
    t.left(angle)
    t.forward(side / 2)
    t.left(180)
    t.forward(side / 2)


def cube(side, angle):
    square(side)
    for i in [180, 90]:
        edge(side, angle)
        t.left(i - angle)
        t.forward(side)
    t.left(90)
    edge(side, angle)
    t.right(angle)
    t.forward(side)
    t.right(180)
    edge(side, angle)
    t.right(angle + 90)
    t.forward(side)
    t.right(90 - angle)
    t.forward(side / 2)
    t.right(angle)
    square(side)

for j in range(0,360,20):
    cube(20, j)
    t.clear()
    t.penup()
    t.home()
    t.pendown()
