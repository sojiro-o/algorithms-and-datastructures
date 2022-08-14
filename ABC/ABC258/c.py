import sys

# テスト入力用
# import io
# _INPUT = u"""\
# 10 8
# dsuccxulnl
# 2 4
# 2 7
# 1 2
# 2 7
# 1 1
# 1 2
# 1 3
# 2 5
# """
# sys.stdin = io.StringIO(_INPUT)

lines = [s.strip() for s in sys.stdin.readlines()]
N, Q = map(int, lines[0].split())
S = str(lines[1])

point = N - 1 # 末尾から何番目の数が先頭として扱われるか 0 based indexing

for line in lines[2:]:
    t, x = map(int, line.split())
    if t == 1:
        point += x
        point %= N # 一周した場合は末尾に戻る
    elif t == 2:
        region_of_head = (N-1) - point
        ans_point = (region_of_head + (x-1)) % N
        print(S[ans_point])


