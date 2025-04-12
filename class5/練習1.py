# 畫星星形狀練習
import turtle as t

t.pensize(5)
t.speed(1)
t.pencolor("yellow")
t.fillcolor("yellow")
t.begin_fill()
for i in range(5):
    t.right(144)
    t.forward(200)
t.end_fill()
t.done()
