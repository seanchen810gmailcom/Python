# append 在程式執行的過程當中可以將資料加入到列表的最後面
l = ["hello", "world"]
l.append("python")  # 加入Python
print(l)  # ['hello', 'world', 'python']

# insert 在程式執行的過程當中可以將資料加入到列表的指定位置
l = ["hello", "world"]
l.insert(1, "python")  # 加入Python
print(l)  # ['hello', 'python', 'world']

# 修改特第未置的資料
l = ["hello", "world"]
l[1] = "python"  # 將索引1的資料改成python
print(l)  # ['hello', 'python']
