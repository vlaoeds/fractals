import turtle as t

def Koh(depth, len):
    if depth == 0:
        return t.forward(len/3)

    Koh(depth - 1, len/3)
    t.left(60)
    Koh(depth - 1, len/3)
    t.right(120)
    Koh(depth - 1, len/3)
    t.left(60)
    Koh(depth - 1, len/3)

n = int(input())
b_len = 1000
t.goto(0,0)
t.tracer(0,0)
for i in range(3):
    Koh(n, b_len)
    t.right(120)
t.update()
t.done()

