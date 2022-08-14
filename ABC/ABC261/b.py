import sys

# テスト入力用 readlineの上に配置する
# import io
# _INPUT = u"""\
# 4
# -WWW
# L-DD
# LD-W
# LDW-
# """
# sys.stdin = io.StringIO(_INPUT)

lines = [s.strip() for s in sys.stdin.readlines()]

N = int(lines[0])
matrix = [list(map(str, x)) for x in lines[1:]]

def battle(x):
    if x == "W":
        return "L"
    elif x == "L":
        return "W"
    else:
        return "D"


# 右上を基準に左下と一致するか見る
# 0 based indexing
for line in range(N):
    # 行毎に見る
    for col in range(line+1, N):
        if battle(matrix[line][col]) != matrix[col][line]:
            print("incorrect")
            exit()

print("correct")