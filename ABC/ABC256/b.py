import sys

# # テスト入力用 readlineのしたに配置する
# import io
# _INPUT = u"""\
# 10
# 2 2 4 1 1 1 4 2 2 1
# """
# sys.stdin = io.StringIO(_INPUT)


lines = [s.strip() for s in sys.stdin.readlines()]

N = int(lines[0])
A = list(map(int, lines[1].split()))

base = [0, 0, 0, 0] # マス0~3の人数
point = 0

for a in A:
    base[0] += 1
    last_base = base
    if a == 4:
        point += sum(base)
        base = [0, 0, 0, 0] # 初期化
    elif a == 3:
        point += sum(base[1:])
        base = [0, 0 ,0 , last_base[0]]
    elif a == 2:
        point += sum(base[2:])
        base = [0, 0 ,last_base[0] , last_base[1]]
    elif a == 1:
        point += sum(base[3:])
        base = [0, last_base[0] ,last_base[1] , last_base[2]]

print(point)