import sys

# テスト入力用 readlineの上に配置する
# import io
# _INPUT = u"""\
# 2 12
# """
# sys.stdin = io.StringIO(_INPUT)


lines = [s.strip() for s in sys.stdin.readlines()]
N, X = map(int, lines[0].split())