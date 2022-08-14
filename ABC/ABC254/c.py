import sys
import bisect

# テスト入力用 readlineの上に配置する
# import io
# _INPUT = u"""\
# -555555555555555555 -1000000000000000000 1000000 1000000000000
# """
# sys.stdin = io.StringIO(_INPUT)


lines = [s.strip() for s in sys.stdin.readlines()]
X, A, D, N = map(int, lines[0].split())

S = []
for i in range(N):
    S.append(A+i*D)

index =  bisect.bisect_left(S,X)

if 0 < index < len(S):
    print(min(S[index]-X, X-S[index-1]))
elif index == 0:
    print(S[0]-X)
else:
    print(X-S[-1])