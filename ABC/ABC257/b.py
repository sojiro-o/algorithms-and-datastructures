import sys

# テスト入力用 readlineのしたに配置する
# import io
# _INPUT = u"""\
# 10 6 9
# 1 3 5 7 8 9
# 1 2 3 4 5 6 5 6 2
# """
# sys.stdin = io.StringIO(_INPUT)

lines = [s.strip() for s in sys.stdin.readlines()]

N, K, Q = map(int, lines[0].split())
A = list(map(int, lines[1].split())) # 0 based indexで左から何番目の駒がどこにあるかを示すものとして使う
L = list(map(int, lines[2].split()))

for l in L:
    # マスは1 based index
    if A[l-1] == N:
        continue
    elif l == K:
        A[l-1] += 1
    elif A[l-1] + 1 == A[l]:
        continue
    else:
        A[l-1] += 1

print(*A)