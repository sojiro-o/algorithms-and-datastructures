import sys

# テスト入力用 readlineの上に配置する
# import io
# _INPUT = u"""\
# 2 1
# 90 80
# 70 60
# """
# sys.stdin = io.StringIO(_INPUT)


lines = [s.strip() for s in sys.stdin.readlines()]
R, C = map(int, lines[0].split())
A = []
A.append(list(map(int, lines[1].split())))
A.append(list(map(int, lines[2].split())))

print(A[R-1][C-1])