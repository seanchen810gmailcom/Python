"""
使用turtle模組+for迴圈
蓋出螺旋狀的印章
"""

# 參考code
import turtle as t

t.speed(0)
t.penup()
t.color("green")
t.shape("turtle")
for i in range(1, 200, 5):
    t.forward(i)
    t.stamp()
    t.right(32)

t.done()
