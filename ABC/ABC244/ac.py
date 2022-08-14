from cmath import nanj
import io
import sys

_INPUT = u"""\
3 5
99999
91919
99989
"""
# if len(__file__.split("/")) >= 3:
sys.stdin = io.StringIO(_INPUT)

# acc new abc160
# oj t -c "python main.py"
    
# lines = [list(map(int, s.strip().split())) for s in sys.stdin.readlines() if s!="\n"]
lines = [s.strip() for s in sys.stdin.readlines() if s!="\n"]

n,m=map(int,lines[0].split())

anm = []
for i in range(n):
    anm.append(lines[i+1])


ans = 0
for i in range(1, 10):
    # i=2
    sl = [[0]*m for _ in range(n)]
    for s in sl[0]:
        s = 0
    for k in sl[m-1]:
        k = 0
    for e in range(n):
        

    mizu = []
    for j in range(n):
        for k in range(m):
            if int(anm[j][k]) >= i:
                sl[j][k]=1
            else:
                mizu.append((j,k))
    if len(mizu)==0:#そもそも全部埋まってるとき
        continue
    
    
    flag=1
    while flag: # 排出され続けるまで
        flag=0
        for index, (mj,mk) in enumerate(mizu):
            if (mj==0) or (mj==n-1):
                del mizu[index]
                flag=1
                continue
            if (mk==0) or (mk==m-1):
                del mizu[index]
                flag=1
                continue
            dx=[1,0,-1,0]
            dy=[0,1,0,-1]
            h =[0]*4
            
            for l in range(4):
                nj = mj+dx[l]
                nk = mk+dy[l]
                if (sl[nj][nk]) or ((nj,nk) in mizu):
                    h[l]=1
            if not all(h):
                del mizu[index]
                flag=1
                continue
    if len(mizu)==0:
        print(ans)
        exit()
    ans+=len(mizu)
print(ans)
    