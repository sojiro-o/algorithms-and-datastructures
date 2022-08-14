import sys

# テスト入力用
import io
_INPUT = u"""\
4 4
3343
3114
3189
3523
"""
sys.stdin = io.StringIO(_INPUT)


lines = [s.strip() for s in sys.stdin.readlines()]

n, m = map(int, lines[0].split())
# 1が壁、0が水
cup = [[int(i) for i in str(l)] for l in lines[1:]]
situation = [[1]*m for _ in range(n)]

for i in range(2, 10):
    # 2から9までの浅さで水を入れていった場合を考える (今回柱は1以上であるため浅さ1は考えない)
    for 




print(cup)
print()