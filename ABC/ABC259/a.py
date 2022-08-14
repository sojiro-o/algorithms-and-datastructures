import sys

# テスト入力用 readlineの上に配置する
# import io
# _INPUT = u"""\
# 100 10 100 180 1
# """
# sys.stdin = io.StringIO(_INPUT)

lines = [s.strip() for s in sys.stdin.readlines()]

N, M, X, T, D = map(int, lines[0].split())

# index: 年齢、content: 身長
# X歳からN歳までのN-X+1年間身長はT
after = [T] * (N-X+1)
# 0歳からX-1歳までは身長はD cm毎に伸びる. X-1歳の時の身長はT-D cm
# 最初に逆順で求める
before = [(T-D)-i*D for i in range(X)]
before.reverse()

before_after = before + after

print(before_after[M])