import sys
import math

# テスト入力用 readlineの上に配置する
# import io
# _INPUT = u"""\
# -505 191 278
# """
# sys.stdin = io.StringIO(_INPUT)

lines = [s.strip() for s in sys.stdin.readlines()]
a, b, d = map(int, lines[0].split())

cos_d = math.cos(math.radians(d))
sin_d = math.sin(math.radians(d))

x = a*cos_d - b*sin_d
y = a*sin_d + b*cos_d

print(x, y)