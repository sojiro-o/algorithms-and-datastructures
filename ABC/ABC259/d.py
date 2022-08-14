import sys

# テスト入力用 readlineの上に配置する
# import io
# _INPUT = u"""\
# 3
# 0 1 0 3
# 0 0 1
# 0 0 2
# 0 0 3
# """
# sys.stdin = io.StringIO(_INPUT)

lines = [s.strip() for s in sys.stdin.readlines()]
N = int(lines[0])
sx, sy, tx, ty = map(int, lines[1].split())

def find(x):
    # 親が自分自身のノードまで遡る
    if par[x] == x:
        return x
    else:
        par[x] = find(par[x])
        return par[x]

def same(x, y):
    return find(x) == find(y)

def unite(x, y):
    # 元のノード番号の大小で親子関係を決めてしまう
    x = find(x)
    y = find(y)
    if x == y:
        return 0
    if x < y:
        x, y = y, x
    par[x] = y

par = [i for i in range(N)] # 0 based

start_circle = 0
tail_circle = 0

for i, line in enumerate(lines[2:]):
    # ついでにスタートが所属する円を調べる
    x,y,r = map(int, line.split())
    if (sx-x)**2 + (sy-y)**2 == r**2:
        start_circle = i
    if (tx-x)**2 + (ty-y)**2 == r**2:
        tail_circle = i
    
    for _j, line2 in enumerate(lines[2+i+1:],1):
        j = _j + i
        x2,y2,r2 = map(int, line2.split())
        if (r-r2)**2 <= (x-x2)**2+(y-y2)**2 <= (r+r2)**2:
            unite(i, j)

if same(start_circle, tail_circle):
    print("Yes")
else:
    print("No")