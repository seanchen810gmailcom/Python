"""
請使用者輸入身高(公尺)h以及體重(公斤)w
透過下面公式計算出BMI數值並顯示計算結果
bmi = w/h**2
EX:
請輸入身高:1.7
請輸入體重:50
你的BMI為17.301038062283737
"""

print("程式開始")
a = input("請輸入體重:")
b = input("請輸入身高:")
w = float(a)
h = float(b)
bmi = w / h**2
print(f"你的BMI是{bmi}")
