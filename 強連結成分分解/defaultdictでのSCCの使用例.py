#######################################################
'''
注意注意注意注意意注意注意注意意注意注意注意意注意注意注意

defaultdictを使った1オリジンでの実装
再帰の上限を上げないのREになる
PyPy3だとTLEになるpython3だと余裕でAC
PyPy3 → for文が強い
Python3 → 他全てにおいて強い
って感じかな?
'''
#######################################################

import sys
sys.setrecursionlimit(10 ** 9)
input = sys.stdin.readline
# 強連結成分分解(SCC): グラフGに対するSCCを行う
# 入力: <N>: 頂点サイズ, <G>: 順方向の有向グラフ, <RG>: 逆方向の有向グラフ
# 出力: (<ラベル数>, <各頂点のラベル番号>)
def scc(N, G, RG):
    order = []
    used = defaultdict(lambda: 0)
    group = defaultdict(lambda: None)
    def dfs(s):
        used[s] = 1
        for t in G[s]:#頂点隣接リスト
            if not used[t]:
                dfs(t)
        order.append(s)
    def rdfs(s, col): # s:スタートする点、col:グループにつける名前 0,1,2,3...と名付ける
        group[s] = col
        used[s] = 1
        for t in RG[s]:
            if not used[t]:
                rdfs(t, col)
    for i in range(1,N+1): # 非連結な箇所もあるのでfor文を回す。各ノード名が0オリジンで割り当てられてるか、1オリジンかで調節
        if not used[i]:
            dfs(i)
    used = defaultdict(lambda: 0) #rdfsのためにussedを初期化
    label = 0 #グループにつける名前 0,1,2,3...と名付ける
    for s in reversed(order):
        if not used[s]:
            rdfs(s, label)
            label += 1
    return label, group # label:最後のラベル、groupリスト (group[ノード]=所属するグループ)

# 縮約後のグラフを構築
def construct(N, G, label, group):
    G0 = [set() for i in range(label)] # グループ毎の接続関係
    GP = [[] for i in range(label)]  # GP[グループナンバー]:所属するノードリスト
    for v in range(1,N+1): #
        lbs = group[v] # ノードvが所属するグループ。各ノード名が0オリジンで割り当てられてるか、1オリジンかで調節
        for w in G[v]: # ノードvから順方向で直接つながっているノードwがノードvとは異なるグループに所属する場合はグループごとの順方向接続を保存する。
            lbt = group[w]
            if lbs == lbt:
                continue
            G0[lbs].add(lbt)
        GP[lbs].append(v)
    return G0, GP

N, M = map(int, input().split())

from collections import defaultdict
G = defaultdict(lambda: [])
RG = defaultdict(lambda: [])
# input data
for _ in range(M):
    s, t = map(int, input().split())
    G[s].append(t)
    RG[t].append(s)

label, group = scc(N, G, RG)
_, GP = construct(N, G, label, group)

ans = 0
for nodelist in GP:
    ans += int(len(nodelist)*(len(nodelist)-1)/2)
print(ans)