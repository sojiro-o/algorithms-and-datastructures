import sys
from collections import defaultdict

# テスト入力用 readlineの上に配置する
import io
_INPUT = u"""\
6 3
2 7 1 8 2 8
2 10
3 1
5 5
"""
sys.stdin = io.StringIO(_INPUT)

lines = [s.strip() for s in sys.stdin.readlines()]

N, M = map(int, lines[0].split())
X = list(map(int, lines[1].split()))
CY = defaultdict(lambda: 0)
for cy in lines[2:]:
    c,y = map(int, cy.split())
    CY[c] = y

count_n = {} # n回連続して○がでた時の得点.
for i in range(1, N+1):
    if i == 1:
        count_n[i] = X[i-1] + CY[i]
    else: 
        count_n[i] = count_n[i-1] + X[i-1] + CY[i]

print(count_n)

max_list = []
for key, value in count_n.items():
    max_list.append(value/(key+1))

cicle = max_list.index(max(max_list)) + 1
print(cicle)

(N // (cicle+1)) * cicle +  count_n[N % (cicle+1)])