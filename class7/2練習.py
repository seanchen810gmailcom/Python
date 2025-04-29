"""
製作一個倒數計時器(以秒為單位)
使用者可以輸入秒數
當秒數歸0時顯示"時間到”
"""

import time as t

秒數 = int(input("請輸入秒數:"))
while 秒數 != 0:
    print(秒數)
    秒數 -= 1
    t.sleep(1)
else:
    print("時間到")
