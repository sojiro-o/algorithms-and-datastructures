import sys

# テスト入力用 readlineのしたに配置する
# import io
# _INPUT = u"""\
# 1 2 1 1000
# """
# sys.stdin = io.StringIO(_INPUT)


lines = [s.strip() for s in sys.stdin.readlines()]

A,B,C,X = map(int, lines[0].split())

if X <= A:
    print(1)
elif X <= B:
    print(C / (B-(A+1)+1))
else:
    print(0)