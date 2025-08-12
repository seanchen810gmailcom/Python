# 在Python中，\n是換行符號，可以用來分隔字串
# 範例：
print("Hello\nWorld")

# 「新變數,新變數 = 某個list」可以把list分開
# 範例：
a = [1, 2, 3]
b, c, d = a
print(b)
print(c)
print(d)
print("＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝")
# isdigit() 介紹
# 作用：判斷字串是否全部由數字組成。
# 回傳值：True 或 False（布林值）。
# 範例：

print("123".isdigit())  # True，因為都是數字
print("12a".isdigit())  # False，因為有字母
print("１２３".isdigit())  # True，全形數字也算數字
print("-123".isdigit())  # False，有負號就不算純數字
