import turtle as t
def IceF_2(depth, lenght):
    if depth == 0:
        t.forward(lenght);
        return 0;
    IceF_2(depth-1, lenght/2);
    t.left(120);
    IceF_2(depth-1, lenght/4);
    t.left(180);
    IceF_2(depth-1, lenght/4);
    t.left(120);
    IceF_2(depth-1, lenght/4);
    t.left(180);
    IceF_2(depth-1, lenght/4);
    t.left(120);
    IceF_2(depth-1, lenght/2);



depth = int(input());
lenght = int(input());
t.penup();
t.goto(-lenght/2, 0)
t.speed(400)
t.pendown();
IceF_2(depth, lenght);
t.done();

