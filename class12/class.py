# index，尋找指定元素在 List 中第一次出現的位置
# 如果元素不存在會產生錯誤，所以使院前建議先檢查元素是否存在
L = [1, 3, 2, 4, 5]
print(l.index(3))  # 找到數字3在索引位置1

# count 統計抹個元素在List 中總共出現了幾次
# 這個方法很適合用來檢查重複製資料的數量
l = ["hello", "world", "Python", "hello"]
print(l.count("hello"))  # hello 這個字串總共出現兩次

# sort 將list 中的元素進行排序 預設是由小到大（升序排序)
# 注意 這個方法會直接修改原本的 lsit，不會產生新的 list
l = [1, 3, 2, 4, 5]
l.sort()
print(l)

# sort (reverse=True) 將list 中的元素由大到小排序(降序排列)
# reverse=True 參數可以讓排序結果相反
l = [1, 3, 2, 4, 5]
l.sort(reverse=True)
print(l)

# reverse 將 list 中的元素的順序完去顛倒
# 這不是排序！只是把第一個變最後一個，最後一個變第一個
l = [1, 3, 2, 4, 5]
l.reverse()
print(l)

# 和字串有很多相似的操作方式
# 我們可以像操作字串一樣來處理 list

# 合併兩間list: 使用+運算子將兩個list 連接再一起
# 這會產生一個全新的lsit，原本的lsit 不會被改變
l1 = [1, 2, 3]
l2 = [4, 5, 6]
l3 = l1 + l2  # 把l1 和 l2  ˙合併成一個新的lsit
print(l3)

# 重複list 中的內容：使用＊運算子讓list內容重複多次
# 這在需要建立重複資料時很有用
l = [1, 2, 3]
l = l * 3  # 讓list的內容重複3次
print(l)

# 不同資料型態之間的轉太技巧
print(range(10))  # range 物件本身慨不到具體內容，只是一個範圍敘述
print(list(range(10)))  # 使用list() 將range 轉換成可以看到內容的lsit
print(list("hello"))  # 將字串轉換成list，每個字元都會變成獨立的元素

# split: 將一個完整的字串按照指定分隔符號切個乘多個部分
# 這是處理文字資料時非常常用的方法
s = "hello world"
l = s.split(" ")  # 以空白字元作為分隔點來切割字串
print(l)
calendar = "2020/12/25"
l = calendar.split("/")  # 以斜線作為分隔點來切割日期字串
print(l)

# join: 將 list 中的多個字串元素合併成一個完整的字串
# 可以指定要用什麼符號來連接這些元素
l = ["hello", "world"]
s = " ".join(l)  # 用空白字元將list 中的元素連接成一個字串
print(s)
