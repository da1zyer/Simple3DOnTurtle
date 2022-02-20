import turtle

t = turtle.Turtle()
t.speed(100)
side = 100

def right_face(side,angle):
    t.left(angle)
    t.forward(side-angle)
    t.left(90-angle)
    t.forward(side)
    t.left(90+angle)
    t.forward(side-angle)
    t.left(90-angle)
    t.forward(side)

def left_face(side,angle):
    t.right(180 - 2 * angle)
    t.forward(side - 2 * angle)
    t.right(2 * angle)
    t.forward(side)
    t.right(180 - 2 * angle)
    t.forward(side - 2 * angle)

# def left_face(side,angle):
#     t.right(180 - 1.5 * angle)
#     t.forward(side - angle * 1.5)
#     t.right(1.5 * angle)
#     t.forward(side)
#     t.right(180 - 1.5 * angle)
#     t.forward(side - angle * 1.5)


def cube(side,angle):
    right_face(side,angle)
    left_face(side,angle)
    t.home()
    t.left(90+angle*2)
    t.forward(side-2*angle)
    t.right(90+angle*2)
    right_face(side,angle)
    t.home()
    t.left(angle)
    t.forward(side-angle)
    t.right(90+angle)
    left_face

# def cube(side,angle):
#     right_face(side,angle)
#     left_face(side,angle)
#     t.home()
#     t.left(90+angle*1.5)
#     t.forward(side - angle * 1.5)
#     t.right(90+angle*1.5)
#     right_face(side,angle)
#     t.home()
#     t.left(angle)
#     t.forward(side-angle)
#     t.right(90+angle)
#     left_face(side,angle)

for i in range(10,180,24):
    cube(side,i)
    t.penup()
    t.home()
    t.pendown()
    t.clear()




