# 生日快樂邀請卡
"""
小華的生日即將到來，他想要製作一張生日派對的邀
請卡。他已經寫下了日期"2023/10/20"，但他想改成"2023-10-20"
這樣的格式。請問小華應該怎麼做呢？
"""

日期 = input("請輸入日期:")
b = 日期.split("/")
a = "-".join(b)
print(a)
