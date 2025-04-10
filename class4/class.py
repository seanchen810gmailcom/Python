# 會出模組
# turtle # 匯出模組turtle
import turtle as t  # 匯入模組turtle並取名為t

# from turtle import * # 匯入模組turtle的所有指令
# from turtle inport done # 匯入模組turtle的指令done

# done()
# turtle.done()

t.speed(1)  # 設定速度為1
t.forward(100)  # 向前走100公尺
t.right(90)  # 向右轉90度
t.forward(100)  # 向前走100公尺

# 發現turtle一開始面向右邊
t.done()  # 讓視窗不要關閉

# for example
# for的組成有三個部分
# for 迴圈變數 in 範圍:
# 迴圈變數只能活在for迴圈裡面
# 迴圈變數每回紇都會從範圍中取出一個值
for i in range(6):  # range 可以產生一組數字, 0-5
    print(i)

for i in range(1, 6):  # range = 1~5
    print(i)

for i in range(1, 6, 2):  # range = 1,3,5
    print(i)

# 蓋圓形範例
import turtle as t

t.penup()  # 提筆, 這樣就不會畫線但是可以移動
t.color("red")  # 設定線色為紅色
t.shape("turtle")  # 設定線形為烏龜
for i in range(120):
    t.forward(20)
    t.stamp()  # 蓋一個印章
    t.right(10)
t.done()

# 蓋方形範例

import turtle as t

t.penup()  # 提筆, 這樣就不會畫線但是可以移動
t.stamp()  # 蓋一個印章
for i in range(4):
    t.forward(100)  # 向前走100公尺
    t.stamp()  # 蓋一個印章
    t.right(90)  # 向右轉90度
t.done()
