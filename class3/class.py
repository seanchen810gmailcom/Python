# try except
# 錯誤處理
try:
    # 嘗試執行可能會出錯的程式碼
    n = int(input("input a number:"))

except:
    # 如果發生錯誤，執行這段程式碼
    print("You showld input a number")

else:
    # 如果沒有錯誤，執行這段程式碼
    print(n + 1)

try:
    h = float(input("請輸入身高:"))
    w = float(input("請輸入體重:"))
    bmi = w / h**2
    print(f"你的BMI是{bmi}")

except:
    print("請輸入有效的數字")

# 比較運算子
print(1 == 1)  # True, 1等於1
print(1 != 1)  # False, 1不等於1
print(1 < 2)  # True, 1小於2
print(1 > 2)  # False, 1大於2
print(1 <= 2)  # True, 1小於等於2
print(1 >= 2)  # False, 1大於等於2

# 邏輯運算子
# and 代表全部條件都要成立才會回覆True
# or 代表全部條件都要成立才會回覆True
# not 代表反轉條件

print(True and True)  # True, True和True
print(True and False)  # False, True和False
print(False and False)  # False, False和False
print(True or True)  # True, True和True
print(True or False)  # True, True和False
print(False or False)  # False, False和False
print(not True)  # False, 非 True
print(not False)  # True, 非 False

# if elif else 是連續的判斷，只要有一個條件成立，後面的判斷就不會執行
# if 一定要有，elif可以有多個但是選用，else只能有一個但是選用
