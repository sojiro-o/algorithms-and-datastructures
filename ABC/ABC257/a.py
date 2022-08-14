import sys

# テスト入力用 readlineのしたに配置する
# import io
# _INPUT = u"""\
# 2 12
# """
# sys.stdin = io.StringIO(_INPUT)


lines = [s.strip() for s in sys.stdin.readlines()]
N, X = map(int, lines[0].split())
origin = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
S = ""

for alphabet in origin:
    S += alphabet*N

print(S[X-1])