print("程式開始")
a = int(input("請輸入數字:"))
if a % 2 == 0:
    print(f"{a}是偶數")
else:
    print("數字是奇數")

print("程式結束")

print("程式開始")
import turtle as t

t.speed(1)
for i in range(4):
    t.forward(100)
    t.right(90)

t.done()

print("程式結束")
