# 數字加總練習
a = int(input("請輸入數字:"))
sum = 0
for i in range(a + 1):
    sum = sum + i
print("從0加到" + str(a) + "的總和為" + str(sum))
