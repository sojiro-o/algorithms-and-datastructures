import sys

# テスト入力用 readlineのしたに配置する
# import io
# _INPUT = u"""\
# 5
# 10101
# 60 50 50 50 60
# """
# sys.stdin = io.StringIO(_INPUT)

lines = [s.strip() for s in sys.stdin.readlines()]

N = int(lines[0])
S = str(lines[1])
W = list(map(int,lines[2].split()))

# [[大子, 体重]]のリストを作る
data = []
for (s,w) in zip(S,W):
    data.append([int(s),w])

# 体重順に並び替える
data = sorted(data, key=lambda x: x[1])
# 体重だけを保存する
w_data = [x[1] for x in data]
# 大子だけ保存する
s_data = [x[0] for x in data]

# 前の体重
before = 0
left = 0
right = sum(s_data)

# 大人N人と予測している
error = N - right

for i in range(N):
    if before == w_data[i]:
        left += s_data[i]
        right -= s_data[i]
        continue
    else:
        # i番目とi+1番目の間で区切る (i番目は子供)
        left += s_data[i]
        right -= s_data[i]
        # 子供i+1人、大人N-(i+1)と予測
        new_error = left + abs((N-(i+1))-right)
        error = min(error, new_error)
        before = w_data[i]

print(N-error)