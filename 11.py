import turtle as t
import math

def Dragon_L(depth, lenght):
    if depth == 0:
        t.forward(lenght);
        return 0;
    t.right(45);
    Dragon_R(depth-1, lenght/math.sqrt(2));
    t.left(90);
    Dragon_L(depth-1, lenght/math.sqrt(2));
    t.right(45);

def Dragon_R(depth, lenght):
    if depth == 0:
        t.forward(lenght);
        return 0;
    t.left(45);
    Dragon_R(depth - 1, lenght/math.sqrt(2));
    t.right(90);
    Dragon_L(depth - 1, lenght/math.sqrt(2));
    t.left(45);


depth = int(input());
lenght = int(input());
t.penup();
t.goto(-lenght/2, 0)
t.speed(400)
t.pendown();
Dragon_R(depth, lenght);
t.done();

