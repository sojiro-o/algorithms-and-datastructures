import sys

# テスト入力用 readlineの上に配置する
# import io
# _INPUT = u"""\
# 6 2 3 3
# """
# sys.stdin = io.StringIO(_INPUT)

lines = [s.strip() for s in sys.stdin.readlines()]
X, A, D, N = map(int, lines[0].split())

if D == 0:
    print(A-X)
    exit()

# 初項を公差で割る
a = A // D
b = A % D

if a < (X/D) < a+N:
    print(min((X+b)%D, D-((X+b)%D)))
elif (X/D) <= a:
    print(abs(A-X))
else:
    print(abs(X-(A+D*(N-1))))