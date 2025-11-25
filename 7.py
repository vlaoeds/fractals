import turtle as t
def IceF_1(depth, lenght):
    if depth == 0:
        t.forward(lenght);
        return 0;

    IceF_1(depth-1,lenght/2);
    t.left(90);
    IceF_1(depth-1,lenght/4);
    t.right(180);
    IceF_1(depth-1,lenght/4);
    t.left(90);
    IceF_1(depth-1,lenght/2);


depth = int(input());
lenght = int(input());
t.penup();
t.goto(-lenght/2, 0)
t.speed(400)
t.pendown();
IceF_1(depth, lenght);
t.done();

