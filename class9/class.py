import random  # 這是隨機模組

# random.randrange 設定範圍的方式跟 range 一樣，特性也一樣不包含最後一個數字
# random.randint 的功能是隨機區得一個數字，range 是產生一組數字
print(random.randrange(10))  # 從0~9中隨機取得一個數字
print(random.randrange(1, 10))  # 從1~9中隨機取得一個數字
print(random.randrange(1, 10, 2))  # 從[1,3,5,7,9]中隨機取得一個數字

# random.randint 設定範圍的方式必須要有開始跟結束，且包含最後一個數字
# 不能跳數字抽籤
print(random.randint(1, 10))  # 從1~10中隨機取得一個數字

# list 清單 (lsit)
# list 可以存入很多資料，每筆資料用','分隔
# list 可以存入不同型態的資料
# list 最外層用'[]'包起來
L = [1, 2, 3, 4, 5]  # 數字
print(L)
# 不同型態混合
L = [1, 2, 3, 4, 5, "Hello", ["world"]]  # 數字,字串,list
print(L)

# list 取值
# list 取值方式跟字串一樣，用'[]' 取值
# list 取值方式跟字串一樣，也可以用'[:]' 取值
# list 當中資料的編號(index)都0為開頭
L = [1, 2, 3, 4, 5]
print(L[0])  # 取得第一個值
print(L[1])  # 取得第二個值
print(L[2])  # 取得第三個值

# list 取值方式跟字串一樣，也可以用'[:]' 取值
# 設定範圍的方式跟range很像，不包含最後一個數字
print(L[1:4:2])  # 取出第二個到第四個值，間隔為2個
print(L[0:3])  # 取出第一個到第三個值
print(L[:3])  # 取得第一到第三個值
print(L[3:])  # 取得第四個到最後一個值
print(L[:])  # 取得所有值

# list len 列表長度
L = [1, 2, 3, 4, 5]
print(len(L))  # 取得list長度,也就是list當中幾筆資料

# 務必不要跟index混淆, index 是資料的編號, len是資料的數量

# len 可以搭配 for 迴圈使用來取得list當中所有資料
for i in range(len(L)):  # 這邊的i是index
    print(L[i])

for i in L:  # 這邊的i是資料
    print(i)

# 是使用哪一種方式讀取list當中的資料,要看使用的情境當中會需要index
