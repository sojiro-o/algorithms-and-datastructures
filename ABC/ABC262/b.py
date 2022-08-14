import sys
import itertools

# テスト入力用 readlineの上に配置する
# import io
# _INPUT = u"""\
# 7 10
# 1 7
# 5 7
# 2 5
# 3 6
# 4 7
# 1 5
# 2 4
# 1 3
# 1 6
# 2 7
# """
# sys.stdin = io.StringIO(_INPUT)

lines = [s.strip() for s in sys.stdin.readlines()]
N, M = map(int, lines[0].split())
edge = [[] for _ in range(N+1)]
for uv in lines[1:]:
    u,v = map(int, uv.split())
    edge[u].append(v)
    edge[v].append(u)

def triangle(a,b,c):
    # 与えられた３つの点で三角形を作れるか
    if (a in edge[b]) & (b in edge[c]) & (c in edge[a]):
        return 1
    else:
        return 0

ans = 0
for points in itertools.combinations(range(1,N+1),3):
    # 3つの点で三角形を作れるか
    ans += triangle(*points)
    
print(ans)
