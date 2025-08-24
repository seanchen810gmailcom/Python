# Python 字串格式化：str.format()

# 用法一：基本用法－用{}佔位子
print("Hello, {}".format("World"))  # Hello, World，因為World 被format()填到{}位置
# {}當作佔位符，代表等一下要用format()的方式填到那個位置
# 也可以像這樣子：
print("{} + {} = {}".format(2, 3, 2 + 3))  # 2 + 3 = 5

# 用法二：位置參數－用數字指定
print("{0} and {1}".format("cat", "dog"))  # cat and dog
print("{1} and {0}".format("cat", "dog"))  # dog and cat
# 在{}裡面加上編號，代表順序

# 用法三：關鍵字參數－用名稱指定
print("Name: {name}, Age: {age}".format(name="Tom", age=12))  # Name: Tom, Age: 12
# 在{}裡面加上關鍵字，接著在format()裡面加入名稱=你要加的東西


# 對齊欄位寬度

# > 右對齊, < 左對齊, ^ 置中
print("|{:>5}|".format(7))  # |    7|
print("|{:<5}|".format(7))  # |7    |
print("|{:^5}|".format(7))  # |  7  |
ㄅ

#  浮點數控制

# , 加上千分位逗號
print("{:,}".format(1234567))  # 1,234,567
# 也可以加入其他東西，像是：
print("{:_}".format(1234567))  # 1_234_567
# 進位制表示
print("{:b}".format(42))  # 101010 (二進位)
print("{:o}".format(42))  # 52     (八進位)
print("{:x}".format(42))  # 2a     (十六進位小寫)
print("{:X}".format(42))  # 2A     (十六進位大寫)
# format()裡面的東西可以改變，像是：
print("{:b}".format(33))  # 100001 (二進位)
print("{:o}".format(55))  # 77     (八進位)
print("{:x}".format(564375))  # d0a    (十六進位小寫)
print("{:X}".format(93))  # 5D     (十六進位大寫)
"""
:b 二進位
:o 八進位
:x 十六進位小寫
:X 十六進位大寫
"""


# 百分比表示

# 自動乘以 100 後加 %
print("{:.1%}".format(0.1234))  # 12.3%
