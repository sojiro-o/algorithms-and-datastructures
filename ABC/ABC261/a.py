import sys

# テスト入力用 readlineの上に配置する
# import io
# _INPUT = u"""\
# 0 3 3 7

# """
# sys.stdin = io.StringIO(_INPUT)

lines = [s.strip() for s in sys.stdin.readlines()]

L1, R1, L2, R2 = map(int, lines[0].split())
LR1 = [i for i in range(L1, R1+1)]
LR2 = [i for i in range(L2, R2+1)]
LR1 = set(LR1)
LR2 = set(LR2)

LR12 = LR1 & LR2

print(max(0, len(LR12)-1))
