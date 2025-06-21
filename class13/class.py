# 字典 （Dictionary）: 用來儲存「key-value」配對的資料結構
# 字典很適合用來表示有對應關西的資料，像是商品價格的對應
# 錯號是不能重複的

# 建立字典：使用大括號 {} , key 和value 之間用冒號: 分隔
d = {"蘋果": 20, "香蕉": 30, "橘子": 25}
print(d)

# 從字典中取得特定 key 對應的 value
# 如果key 不存在會產生 key error 錯誤
d = {"蘋果": 20, "香蕉": 30, "橘子": 25}
print(d["蘋果"])
# print(d["梨"])  # 這行會產生 key error:'梨子 錯誤
# print(d["梨子"])  # 這行會產生 key error:'梨子 錯誤

# 編歷字典：有多種方式可以走訪字典中的資料
d = {"蘋果": 20, "香蕉": 30, "橘子": 25}

# 方式一：直接編歷字典，會取得所有key
for k in d:
    print(k)  # 印出 key 名稱
    print(d[k])  # 用key 來取得對應的 value

#  方式二：明確使用keys() 方法來取得所有key
for k in d.keys():
    print(k)  # 印出key 名稱
    print(d[k])  # 用key 來取得對應的 value

# 方式三：使用valus() 方法來取得所有value
for v in d.values():
    print(v)  # 直接印出value , 但不知道對應的 key 是什麼

# 方式四：使用 items() 方法同時取得 key 和 value
# 這是最常用的方式 , 因為可以同時取得 key 和 value
for k, v in d.items():
    print(f"{k};{v}")  # 同時印出 key 和 value 的配對關西


# 新增/修改字典的內容
# 直接指定 key 對應的 value, 如果 key 已存在就是修改, 如果 key 不存在則是新增
d = {"蘋果": 20, "香蕉": 30, "橘子": 25}
d["蘋果"] = 10  # 修改 [蘋果] 對應的 vallue
print(d)
d["蓮霧"] = 15  # 新增一個 key-value 配對
print(d)

# 刪除字典的內容
d = {"蘋果": 20, "香蕉": 30, "橘子": 25}
d.pop("蘋果")  # 刪除蘋果
# 如果要刪掉的key 不存在，會出現key Error,所以可以加上第二個參數,當key不存在時，不會有任何變化
popitem = d.pop("蓮霧" "不存在這筆資料")  # 不會有任何變化
print(d)  # ('香蕉', 30'橘子', 25)
print(popitem)  # 不存在這筆資料


# len :取得字典中有多少組 key-value 配對
d = {"蘋果": 20, "香蕉": 30, "橘子": 25}
print(len(d))

# 檢查某個 key 是否 存在於字典中
# 使用前先檢查可以避免 key error 錯誤
d = {"蘋果": 20, "香蕉": 30, "橘子": 25}
print("蘋果" in d)  # True, 蘋果這個key 存在
print("蓮霧" in d)  # False, 蓮霧這個key 不存在


# 檢查某個元素有沒有在list中
# 使用 in 可以快速檢查某個元素是否存在於list中
l = [1, 2, 3, 4, 5]
print(2 in l)  # True, 3 在 list 中
