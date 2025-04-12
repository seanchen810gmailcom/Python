"""
使用turtle 繪製時鐘
"""

import turtle as t
import time

a = 0
t.speed(0)
t.left(90)
for i in range(61):
    t.forward(100)
    t.home()
    t.clear()
    time.sleep(1)
    a = int(a + 1)
    b = int(6 * a)
    t.left(90 - b)

t.done()
