"""
請輸入要印出的箭頭大小
hint:
可利用字串乘法
>>>val="*" * 3
>>>print(val)
>>>***
EX:
請輸入要印出的箭頭大小:3
  *
 ***
*****
  *
  *
  *
"""

a = int(input("請輸入要印出的箭頭大小:"))
for i in range(a + 1):
    print("*" * i)
for i in range(a):
    print("*")
5
