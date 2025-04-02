password = input("請輸入密碼:")
if password == "3.1415926":
    print("Hi陳宥翔")
elif password == "?????????":
    print("HISean")
else:
    print("密碼錯誤")
    print("BBBBBBBBBBBBBBBB")

成績1 = input("請輸入成績:")
成績2 = float(成績1)
if 成績2 >= 90:
    分數 = "A"
elif 成績2 >= 80:
    分數 = "B"
elif 成績2 >= 70:
    分數 = "C"
elif 成績2 >= 60:
    分數 = "D"
else:
    分數 = "E"
print(f"你的成績是{分數}")
