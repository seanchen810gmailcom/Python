# def
# 新增一個函數要用def開頭,後面接著函數名稱,再加上小括號,最後加上冒號。
# 小括號裡面可以放入傳入函數的參數，也可以不放。
def hello():
    print("Hello World")


for i in range(10):
    hello()


# 有傳入參數的函數
# 這個函數有一個參數 name，當呼叫這個函數時，可以傳入一筆資料給 name。
def hello(name):
    print(f"hello, {name}!")


hello("Alice")
hello("Bob")
hello("Charlie")
for i in range(10):
    hello(i)  # 這裡有 i 會被當作 name 的值


# 有回傳值的函數
# 這個函數會回傳一個值，當呼叫這個函數時，可以把回傳的值存起來。
# 在指令當終止要執行return就可以回傳值，並結束函數
def add(a, b):  # 可以允旭多個傳入參數
    return a + b


print(add(1, 2))
print(add("hello,", "world!"))
sum = add(3, 4)  # 可以將回傳值存到變數中
print(sum)


# 有多個回傳值的函數
# 這個函數換回傳兩個值，當呼叫這個函數，可以把回傳的值存起來
def add_sub(a, b):
    return a + b, a - b


sum, sub = add_sub(5, 6)  # 可以將回傳值存到多個變數中
print(f"sum={sum}, sub={sub}")


# 多個return
def add_sub(a, b):
    if a > b:
        return a + b
    else:
        return a - b


print(add_sub(5, 6))
print(add_sub(6, 5))


# 預設參數
# 可以在函數的猜數中設定預設值，當呼叫這個函數時，如果沒有傳入參數，就會使用預設值。
# 多個參數時，有預設值的參數要放在沒有預設值的參數後面。
def hello(name, massage="Hello"):
    print(f"{massage}, {name}!")


# 如果是 def hello（message="hello",name）會出錯，因為有預設值的參數要放在沒有預設值的參數後面。
hello("Alice")
hello("Bob", "Good morning")


# def 區域變數與全域變數
length = 5  # 全域變數


def calculate_square_area():
    area = length**2  # length 是全域變數，area是區域變數
    # length = length + 1 # 這行會出錯
    # 因為在函數內部length是區域變數,不能直接修改全域變數
    print("面積是", area)


calculate_square_area()
# print("長度是",area)# 這行會出錯，因喔area是區域變數，只能在函數內部使用

length = 5  # 全域變數


def calculate_square_area():
    area = length**2  # length 是全域變數，area是區域變數
    print("面積是", area)


length = 10  # 全域變數
calculate_square_area()  # 面積是 100
