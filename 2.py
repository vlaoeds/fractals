import turtle as t
def bi_tree(hieght, angle, b_len):
    if hieght == 0:
        return 0
    t.forward(b_len)
    t.right(angle)

    bi_tree(hieght - 1, angle, b_len * 0.8)
    t.left(2*angle)

    bi_tree(hieght - 1, angle, b_len * 0.8)
    t.right(angle)
    t.backward(b_len)



h, a = map(int, input().split())
b_len = 100
t.goto(0,0)
t.left(90)
t.speed(1)
bi_tree(h, a, b_len)
t.done()

