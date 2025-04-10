"""
使用turtle模組+for迴圈
蓋出螺旋狀的印章
"""

# 參考code
import turtle as t

t.penup()
t.color("red")
t.shape("circle")
for i in range(1, 200, 5):
    t.forward(i)
    t.stamp()
    t.right(32)

t.done()
