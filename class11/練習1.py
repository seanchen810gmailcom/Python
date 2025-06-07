print("購物清單:")
清單 = []
print("目前清單是空的")
while True:
    print(清單)
    print("功能清單：")
    print("1.新增東西")
    print("2.修改東西")
    print("3.刪除東西")
    print("4.離開系統")
    要做的事 = input("請輸入您的選擇:")
    if 要做的事 == "1":
        print("新增選單：")
        print("a.加到尾端")
        print("b.插入指定位置")
        方法 = input("請選擇方法（a,b):")
        if 方法 == "a":
            新增東西 = input("請輸入新增的東西:")
            清單.append(新增東西)
        elif 方法 == "b":
            插入位置 = int(input("請輸入插入位置(開頭是0):"))
            新增東西 = input("請輸入新增的東西:")
            清單.insert(插入位置, 新增東西)
    elif 要做的事 == "2":
        修改編號 = int(input("請輸入您要修改的編號:"))
        新增東西 = input("請輸入新增的東西:")
        清單[修改編號] = 新增東西
    elif 要做的事 == "3":
        print("刪除選單：")
        print("a.依名稱刪除")
        print("b.一編號刪除")
        刪除方法 = input("請選擇方法（a,b):")
        if 刪除方法 == "a":
            刪除名稱 = input("請輸入刪除的名稱:")
            清單.remove(刪除名稱)

        elif 刪除方法 == "b":
            刪除編號 = int(input("請輸入刪除的編號:"))
            清單.pop(刪除編號)

    elif 要做的事 == "4":
        print("歡迎下次再期待!")
        break
