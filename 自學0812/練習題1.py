for num in range(1, 11):
    if num % 2 == 0:
        continue  # 偶數跳過
    if num > 7:
        break  # 大於7停止
    print(num)
