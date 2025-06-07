# 複製 List，避免原本的List被更動
L = ["hello", "world"]
L2 = L.copy()  # 使用copy() 複製list
print(L2)  # ['hello', 'world']
L2[0] = "python"  # 修改複製後List的索引 0資料
print(L)  # ['hello', 'world'] 原本的List 不受影響
print(L2)  # ['python', 'world']只有複製的List 被改變
# 這跟變數的=賦值不同，一般情況下會開2個記憶體空間，
# 在List的情況下使用=會讓兩個變數名稱指向同一個記憶體空間，
# 這個導至修改一個List會影響到另一個List。
# 所以在需要複製List時，應該使用copy()方法。


# remove：移除List中指定的元素（只會移除第一個抓到的）
L = ["Hello", "World", "Python"]
L.remove("World")  # 移除"whrld"
print(L)  # ['Hello', 'Python']

# pop：移除並回傳 List 中的元素
L = ["Hello", "World", "Python"]
# 不給索引時.pop() 會移除最後一個元素
L.pop()  # 移動最後一個元素
print(L)  # ['Hello', 'World']
s = L.pop(1)  # 移除索引1 的元素，並回傳該值
