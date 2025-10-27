import turtle
start_len = int(input())
depth_rec = int(input())
turtle.speed(300)
def square(x, y):
    counter = 0
    while counter < 4:
        turtle.forward(x)
        turtle.right(90)
        counter += 1
    turtle.penup()
    turtle.right(9)
    turtle.forward(x/10)
    turtle.pendown()
    if y == 0:
        return 0
    else: square(x - x/10, y - 1)

turtle.goto(0,0)
turtle.pendown()
square(start_len, depth_rec)

turtle.done()