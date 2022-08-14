import sys

# テスト入力用 readlineのしたに配置する
# import io
# _INPUT = u"""\
# 4
# 1161
# 1119
# 7111
# 1811
# """
# sys.stdin = io.StringIO(_INPUT)


lines = [s.strip() for s in sys.stdin.readlines()]
N = int(lines[0])
A = [[int(i) for i in x] for x in lines[1:]]

# ４つ繋げることで全て財源可能
AA = [a+a for a in A]
AAAA = AA+AA

ans_candidate = []

# 行の和
for gyo in A:
   ans_candidate.append(gyo)
# 列の和
for retu in range(N):
    miti = []
    for gyo in A:
        miti.append(gyo[retu])
    ans_candidate.append(miti)
# /の和
for i in range(2, N*2-2):
    miti = []
    for j in range(N):
        miti.append(AA[j][i-j])
    ans_candidate.append(miti)

# \の和
for i in range(N):
    miti = []
    for j in range(N):
        miti.append(AA[j][i+j])
    ans_candidate.append(miti)

ans_candidate2 = []
for i in ans_candidate:
    i2 = i + i
    for j in range(N):
        x = ""
        for k in range(N):
            x += str(i2[j+k])
        y = int(x[::-1])
        x = int(x)
        ans_candidate2.append(x)
        ans_candidate2.append(y)
print(max(ans_candidate2))