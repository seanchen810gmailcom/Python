# ===== Matplotlib 中文完全筆記 (macOS 適用) =====
import matplotlib.pyplot as plt
import matplotlib

# ---- 中文字體設定 (macOS 必加，不然會變方框) ----
matplotlib.rcParams["font.family"] = "PingFang TC"  # macOS 內建中文字體
matplotlib.rcParams["axes.unicode_minus"] = False  # 修正負號顯示

# ---- 基本範例 ----
x = [1, 2, 3, 4, 5]
y = [1, 4, 9, 16, 25]

plt.plot(x, y)  # 畫折線圖
plt.show()  # 顯示圖表

# ===== 常見圖表類型 =====
plt.plot(x, y)  # 折線圖
plt.scatter(x, y)  # 散點圖
plt.bar(x, y)  # 長條圖
plt.hist(y, bins=5)  # 直方圖
plt.pie([10, 20, 30, 40])  # 圓餅圖
plt.show()

# ===== 標題與標籤 =====
plt.plot(x, y)
plt.title("平方函數")  # 標題
plt.xlabel("X 軸")  # X 軸名稱
plt.ylabel("Y 軸")  # Y 軸名稱
plt.show()

# ===== 多條線 =====
y2 = [2, 4, 6, 8, 10]
plt.plot(x, y, label="平方數")
plt.plot(x, y2, label="2x")
plt.legend()  # 顯示圖例
plt.show()

# ===== 自訂樣式 =====
plt.plot(x, y, color="red", linestyle="--", marker="o")
plt.show()

# ===== 多張圖 (子圖) =====
plt.subplot(1, 2, 1)  # 1列2欄，左邊
plt.plot(x, y)

plt.subplot(1, 2, 2)  # 右邊
plt.bar(x, y)

plt.show()

# ===== 儲存圖片 =====
plt.plot(x, y)
plt.savefig("my_plot.png")  # 存成 PNG
plt.savefig("my_plot.pdf")  # 存成 PDF

# ===== 進階功能 =====
# 3D 繪圖
from mpl_toolkits.mplot3d import Axes3D

fig = plt.figure()
ax = fig.add_subplot(111, projection="3d")
ax.plot([1, 2, 3], [4, 5, 6], [7, 8, 9], [3, 5, 4], [1, 2, 3])
plt.show()

# (進階) 動畫: 使用 matplotlib.animation.FuncAnimation
# (進階) 影像處理: plt.imshow(img) 可顯示圖片

# ===== 常用對照表 =====
# Marker (點樣式)
# "o"  圓形   "s"  正方形   "^"  三角形(上)   "v" 三角形(下)
# "*"  星星   "+"  加號     "x"  叉號         "." 小點
# ","  超小點

# Color (顏色)
# "r"=red(紅)  "g"=green(綠)  "b"=blue(藍)  "c"=cyan(青)
# "m"=magenta(洋紅) "y"=yellow(黃) "k"=black(黑) "w"=white(白)
# 也可用 16進位色碼: "#FF5733"

# Linestyle (線型)
# "-"  實線   "--" 虛線   "-." 點劃線   ":" 點點線

# ===== 學習順序建議 =====
# 1. 先學 基本折線圖、長條圖、散點圖
# 2. 加上 標題、座標軸名稱、圖例
# 3. 玩顏色、線條、點樣式
# 4. 學多張圖 (subplot) 與排版
# 5. 挑戰 3D 繪圖與動畫
