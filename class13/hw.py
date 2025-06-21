print("＝＝＝水果電價格查詢幾＝＝＝")
水果 = {"蘋果": 10, "香蕉": 20, "橘子": 25}
while True:
    print("目前水果價格")
    for 水果名稱, 水果價錢 in 水果.items():
        print(f"{水果名稱}:{水果價錢}元")
    print("1. 新增水果價格")
    print("2. 修改水果價格")
    print("3. 刪除水果")
    print("4. 離開系統")
    功能 = input("請輸入您的選擇:")
    if 功能 == "1":
        新增水果 = input("請輸入新增的水果名稱:")
        if 新增水果 in 水果:
            print("水果名稱已存在!")
            continue

        水果價錢 = input("請輸入新增的水果價格:")
        水果[新增水果] = 水果價錢

    elif 功能 == "2":
        修改水果 = input("請輸入修改的水果名稱:")
        if (修改水果 in 水果) == False:
            print("水果名稱不存在!")
            continue
        水果價錢 = input("請輸入修改的水果價格:")
        水果[修改水果] = 水果價錢
    elif 功能 == "3":
        刪除水果 = input("請輸入刪除的水果名稱:")
        水果.pop(刪除水果)
        if (刪除水果 in 水果) == False:
            print("水果名稱不存在!")
            continue
    elif 功能 == "4":
        print("歡迎下次再期待!")
        break
