fruits = {"蘋果": 20, "香蕉": 15, "西瓜": 50}

while True:
    user_input = input("請輸入：")
    if user_input == "exit":
        print("離開查詢")
        break

    parts = user_input.split()
    if len(parts) != 2:
        print("輸入格式錯誤，請輸入：水果名 數量")
        continue

    fruit_name, quantity_str = parts

    if fruit_name not in fruits:
        print("查無此水果")
        continue

    if not quantity_str.isdigit() or int(quantity_str) <= 0:
        print("數量錯誤")
        continue

    quantity = int(quantity_str)
    price = fruits[fruit_name] * quantity
    print(f"總價格：{price} 元")
print(f"總價格：{price} 元")
