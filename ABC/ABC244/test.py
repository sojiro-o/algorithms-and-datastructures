import sys
import copy

#テスト入力用 readlineのしたに配置する
# import io
# _INPUT = u"""\

# """
# sys.stdin = io.StringIO(_INPUT)


lines = [s.strip() for s in sys.stdin.readlines()]

N = int(lines[0])
T = str(lines[1]).split() # リスト区切り

n = int(lines[2]) # 取引先の数

now = 3 # 現在のindex
querry = [] # 全部の取引情報を三重リストでまとめる[[[a,b] [a,b]   ]     ]

for _ in range(n):
    l = int(lines[now])
    querry2 = []
    for i in range(l):
        querry3 = str(lines[now+1+i]).split() # lの次から格納する
        querry2.append(querry3)
    
    querry.append(querry2)
    now += (l+1)

exist = False
for t in T:
    if t[0] == "#":
        exist = True

if not exist:
    exit(print(" ".join(T)))


for q in querry:
    # exist = False
    T_ = copy.copy(T)
    for convert in q:
        # 書き換え
        T__ = copy.copy(T)
        for i,t in enumerate(T__):
            if t == convert[0]:
                T_[i] = convert[1]
                # exist = True

    out = False
    for t in T_:
        if t[0] == "#":
            out = True
            print("Error: Lack of data")
            break
    
    if out:
        continue

    print(" ".join(T_))
