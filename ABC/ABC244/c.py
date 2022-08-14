import sys

# テスト入力用 readlineのしたに配置する
# import io
# _INPUT = u"""\
# 20
# SRSRSSRSSSRSRRRRRSRR
# """
# sys.stdin = io.StringIO(_INPUT)


lines = [s.strip() for s in sys.stdin.readlines()]

N = int(lines[0])
T = str(lines[1])

location = [0,0]
direction = [[1,0], [0,-1], [-1,0], [0,1]] # 0,1,2,3
now_dir = 0

for t in T:
    if t == "S":
        location[0] += direction[now_dir][0]
        location[1] += direction[now_dir][1]
    else:
        now_dir += 1
        now_dir %= 4

print(location[0], location[1])