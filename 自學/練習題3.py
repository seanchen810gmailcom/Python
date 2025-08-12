scores = {}

while True:
    user_input = input("請輸入學生姓名與分數（空白分隔），或輸入 done 結束：")
    if user_input.lower() == "done":
        break

    parts = user_input.split()
    if len(parts) != 2:
        print("格式錯誤，請重新輸入：名字 分數")
        continue

    name, score_str = parts
    if not score_str.isdigit():
        print("分數必須是數字")
        continue

    score = int(score_str)
    scores[name] = score

print("\n=== 學生成績 ===")
for name, score in scores.items():
    print(f"{name}: {score}")

if scores:
    avg = sum(scores.values()) / len(scores)
    print(f"平均分數：{avg:.2f}")

    print("\n=== 由高到低排序 ===")
    for name, score in sorted(scores.items(), key=lambda x: x[1], reverse=True):
        print(f"{name}: {score}")
