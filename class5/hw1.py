"""
作業說明:
讓turtle蓋出一個時鐘數字的位置
總共會蓋出12個印章
"""

import turtle as t

a = 0
for i in range(8):
    t.speed(0)
    t.penup()
    t.forward(100)
    t.stamp()
    t.home()
    a = a + 1
    t.right(45 * a)
t.done()
