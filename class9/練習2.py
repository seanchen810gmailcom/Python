"""
・請將果汁新增到list並使用list完成之前的功能
juices_list = ["蘋果汁","柳橙汁","葡萄汁","系統關閉"]
"""

l = [
    "1蘋果汁",
    "2柳橙汁",
    "3葡萄汁",
    "4可樂",
    "5雪碧",
    "6蘋果西打",
    "7寶礦力水得",
    "8礦泉水",
    "9梅酒",
    "10黑松沙士" "11系統關閉",
]
while True:
    print(l)
    try:
        a = int(input("請輸入有效數字:"))
    except:
        print("請輸入有選項數字")
    else:
        if a < len(l):
            print(("您輸入的選項為") + (l[a - 1]))
        elif a == len(l):
            print(("您輸入的選項為") + (l[len(l) - 1]))
            break
        else:
            print("請輸入有效的選項")


print("系統結束")
