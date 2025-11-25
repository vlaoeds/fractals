import turtle as t

def Levi_curve(depth, lenght):
    if depth == 0:
        t.forward(lenght);
        return 0;

    t.left(45);
    Levi_curve(depth-1,lenght);
    t.right(90);
    Levi_curve(depth-1, lenght);

depth = int(input());
lenght = int(input());
t.penup();
t.goto(-lenght/2, 0)

t.pendown();
Levi_curve(depth, lenght);
t.done();

