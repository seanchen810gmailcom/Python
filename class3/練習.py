password = input("請輸入密碼:")
if password == "3.1415926":
    print("Hi陳宥翔")
elif password == "?????????":
    print("HISean")
else:
    print("密碼錯誤")
    print("BBBBBBBBBBBBBBBB")

成績1 = input("請輸入成績:")
成績2 = int(成績1)
if 成績2 >= 90:
    print("A")
elif 成績2 >= 80:
    print("B")
elif 成績2 >= 70:
    print("C")
elif 成績2 >= 60:
    print("D")
else:
    print("F")
