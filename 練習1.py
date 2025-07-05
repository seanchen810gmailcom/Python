def add_fruit():
    global 水果
    # 新增水果價格
    新增水果 = input("請輸入新增的水果名稱:")
    if 新增水果 in 水果:
        print("水果名稱已存在!")
        return

    水果價錢 = input("請輸入新增的水果價格:")
    水果[新增水果] = 水果價錢


def change_fruit():
    # 修改水果價格
    global 水果
    修改水果 = input("請輸入修改的水果名稱:")
    if (修改水果 in 水果) == False:
        print("水果名稱不存在!")
        return
    水果價錢 = input("請輸入修改的水果價格:")
    水果[修改水果] = 水果價錢


def delete_fruit():
    # 刪除水果
    global 水果
    刪除水果 = input("請輸入刪除的水果名稱:")
    if 刪除水果 in 水果:
        水果.pop(刪除水果)
    else:
        print("水果名稱不存在!")


# 初始化水果價格字典
水果 = {"蘋果": 10, "香蕉": 20, "橘子": 25}
option = [add_fruit, change_fruit, delete_fruit]

print("＝＝＝水果電價格查詢幾＝＝＝")
while True:
    # 顯示目前數所有水果價格
    print("目前水果價格")
    for 水果名稱, 水果價錢 in 水果.items():
        print(f"{水果名稱}:{水果價錢}元")

    # 顯示功能列表
    print("1. 新增水果價格")
    print("2. 修改水果價格")
    print("3. 刪除水果")
    print("4. 離開系統")

    choice = int(input("請輸入您的選擇:"))
    if choice == len(option) + 1:
        print("歡迎下次再期待!")
        break
    else:
        option[choice - 1]()

    print("=" * 26)
