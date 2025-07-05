print("程式開始")
while True:
    print("=" * 100)
    整數的地方 = int(input("輸入一個整數的地方: "))
    分母的地方 = int(input("輸入一個分母的地方: "))
    分子的地方 = int(input("輸入一個分子的地方: "))
    if 整數的地方 == 0:
        if 分母的地方 == 0:
            if 分子的地方 == 0:
                print("程式結束")
                break

    else:
        分子 = 整數的地方 * 分母的地方 + 分子的地方
        print(f"{分子} /{分母的地方}  ")
