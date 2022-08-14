#!/usr/bin/env python3

import sys

# テスト入力用
import io
_INPUT = u"""\
11
1 20
1 10
1 30
1 20
3 15 1
3 15 2
3 15 3
3 15 4
2 100 5
1 1
2 100 5
"""
sys.stdin = io.StringIO(_INPUT)

input = sys.stdin.readline

from array import array
import bisect

Q = int(input())
query = []
X = set()

for i in range(Q):
    query.append(list(map(int, input().split())))
    X.add(query[i][1]) # Xは集合

X = sorted(X)
print(X)
idx = {x: i for i, x in enumerate(X)}
print(idx)

a = array('I', [])

for q in query:
    c = q[0]
    ix = idx[q[1]]

    if c == 1:
        bisect.insort(a, ix)
    
    elif c == 2:
        k = q[2]
        i = bisect.bisect(a, ix)
        print(X[a[i-k]] if 0 <= i-k else -1) 
    
    elif c == 3:
        k = q[2]
        i = bisect.bisect_left(a, ix)
        print(X[a[i+k-1]] if i+k-1 < len(a) else -1) 
