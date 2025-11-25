import turtle as t

def Minkowski_curve(depth, lenght):
    if depth == 0:
        t.forward(lenght);
        return 0;

    Minkowski_curve(depth-1, lenght/4);
    t.right(90);
    Minkowski_curve(depth-1, lenght/4);
    t.left(90);
    Minkowski_curve(depth-1, lenght/4);
    t.left(90);
    Minkowski_curve(depth-1, lenght/4);
    Minkowski_curve(depth-1, lenght/4);
    t.right(90);
    Minkowski_curve(depth-1, lenght/4);
    t.right(90);
    Minkowski_curve(depth-1, lenght/4);
    t.left(90);
    Minkowski_curve(depth-1, lenght/4);

depth = int(input());
lenght = int(input());
t.penup();
t.goto(-lenght/2, 0)
t.speed(400)
t.pendown();
Minkowski_curve(depth, lenght);
t.done();

