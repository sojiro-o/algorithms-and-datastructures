import sys
from math import dist

# テスト入力用 readlineの上に配置する
# import io
# _INPUT = u"""\
# 4 2
# 2 3
# 0 0
# 0 1
# 1 2
# 2 0
# """
# sys.stdin = io.StringIO(_INPUT)


lines = [s.strip() for s in sys.stdin.readlines()]
N, K = map(int, lines[0].split())
Ak = list(map(int, lines[1].split())) # 1 based indexing

XY_dark = []
XY_light = []

for i, line in enumerate(lines[2:]):
    if (i+1) in Ak: 
        XY_light.append(list(map(int, line.split())))
    else:
        XY_dark.append(list(map(int, line.split())))


XY_dark_lightup = [10**10] * len(XY_dark) # 最小距離を記録

for xy_l in XY_light:
    for i, xy_d in enumerate(XY_dark):
        past_length = XY_dark_lightup[i]
        XY_dark_lightup[i] = min(past_length, dist(xy_l, xy_d))

print(max(XY_dark_lightup))
