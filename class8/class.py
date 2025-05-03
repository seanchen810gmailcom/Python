# break
# 迴圈的 break 可以用來跳出所屬的迴圈，所以判斷break屬於哪個迴圈時，必須要注意縮排
# 例如：

for i in range(5):
    for j in range(5):
        if i == 2 and j == 2:
            break
        print(f"i:{i},j:{j}")
# 這裡的break只會跳出內層的for迴圈，外層的for迴圈還是會繼續執行

# continue
# 這裡的 continue 會跳過 i = 2 的那次迴圈，直接執行i = 3的那次迴圈
# 所以輸出的結果是 0,1,3,4
# 例如：
i = 0
while i < 5:
    if i == 2:
        continue
    print(i)
    i += 1
# continue 也要判斷所屬的迴圈，所以要注意說縮排
