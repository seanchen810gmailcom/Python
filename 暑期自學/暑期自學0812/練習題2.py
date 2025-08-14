fruit = {"蘋果": 20, "香蕉": 15, "西瓜": 50}

while True:
    user_input = input("請輸入：")
    if user_input == "exit":
        print("系統結束")
        break

    parts = user_input.split()
    if len(parts) != 2:
        print("輸入格式錯誤，請輸入：水果名 數量")
        continue

    水果名稱, 水果數量 = parts

    if 水果名稱 not in fruit:
        print("水果不存在")
        print(fruit)
        continue

    if not 水果數量.isdigit():
        print("請輸入正整數")
        continue

    數量 = int(水果數量)
    總價 = fruit[水果名稱] * 數量
    print(f"{水果名稱}的價格是{fruit[水果名稱]}，{數量}個總共是{總價}")
