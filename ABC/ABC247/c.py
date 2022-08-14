import sys
import numpy as np

# テスト入力用 readlineのしたに配置する
import io
_INPUT = u"""\
4
1 2 3
2 2
1 3 4
2 3
"""
sys.stdin = io.StringIO(_INPUT)


lines = [s.strip() for s in sys.stdin.readlines()]

Q = int(lines[0])
cylinder = []
quantity = np.array([0])

for query in lines[1:]:
    if str(query)[0] == "1":
        q,x,c = map(int, query.split())
        cylinder.append([x,c])
        quantity = np.append(quantity, quantity[-1]+c)
    
    else:
        print(cylinder)
        q,c = map(int, query.split())
        # ギリギリ小さいところまで二分探索, indexは大きめ
        index = np.searchsorted(quantity, c, side="left")
        index -= 1
        print(quantity, c)
        amari = quantity[index+1] - c
        print("amari",amari)
        quantity = quantity[index:] - c
        ans = 0
        for i in range(0,index):
            ans += cylinder[i][0] * cylinder[i][1]
        print(index)
        cylinder[index][1] -= amari
        ans += cylinder[index][0] * cylinder[index][1]

        cylinder = cylinder[index:]
        print("ans",ans)