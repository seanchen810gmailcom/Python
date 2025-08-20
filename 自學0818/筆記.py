# \' 單引號：
# 可以在不被終端機誤會的狀態下寫單引號
# 舉例：
print("I can't do it")  # I can't do it
# \\ 反斜線
# 因為如果寫\會被終端機誤會成跳脫字元，所以必須寫兩個才會讓終端機知道你要寫一個反斜線
# \r 回車
# 會在print到終端機看到\r這個符號的時候把游標移到前面，本來寫的文字會－被覆蓋掉
# 舉例1：
print(
    "Hello\rWorld"
)  # World 只出現World是因為Hello和World的字數一樣，所以會剛好完全被覆蓋掉！
# 舉例2：
print(
    "Hello\rHi"
)  # Hillo 因為Hi的字數比Hello小，所以Hi沒辦法完全覆蓋掉Hello，所以會變成Hillo
print("world\rHiHiHi")  # HiHiHi HiHiHi 的字數比world多，所以也可以覆蓋掉整個world字
# \v 垂直定位
# 通常會換行+縮排
# 舉例：
print("Hello\vWorld")  # Hello
# \b 刪除一個字元
# 跟電腦的backspace按鍵很像，可以刪除他左邊的一個字元
# 舉例：
print("Helloo\bWorld")  # HelloWorld，因為Helloo的第二個o被刪除了
# \" 雙引號
# 可以在不被終端機誤會的狀態下寫雙引號
# 舉例：
print('"I can\'t do it"')  # "I can't do it"
# \n 換行
# 可以在print裡面加上\n，讓print的時候換行
# 舉例：
print("Hello\nWorld")  # Hello
# World
# \t 水平定位 (Tab)
# 可以在print裡面加上\t，讓print的時候出現Tab空格
# 舉例：
print("Hello\tWorld")  # Hello   World
# \a 響鈴
# 因為vscode是模擬器，所以會省略發出聲音
# 方法：
"""
1.打開apple 終端機
2.在終端機中輸入「python3」
3.終端機會有這個讓你輸入的地方(<<<)
4.在後面輸入print("響鈴\a")
5.電腦就會發出提示音
"""
# 注意事項：
"""
如果讓他執行響鈴超過5次電腦就會視為很吵，後面的就會自動抵銷，所以如果你要讓他叫超過五次就必須這樣子寫：
import time as t
for i in range(10):
    print("響鈴\a")
    t.sleep(0.5)
"""
