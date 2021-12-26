# 強連結成分分解(SCC): グラフGに対するSCCを行う
# 入力: <N>: 頂点サイズ, <G>: 順方向の有向グラフ, <RG>: 逆方向の有向グラフ
# 出力: (<ラベル数>, <各頂点のラベル番号>)
def scc(N, G, RG):
    order = []
    used = [0]*N
    group = [None]*N
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
    for i in range(N): # 非連結な箇所もあるのでfor文を回す
        if not used[i]:
            dfs(i)
    used = [0]*N #rdfsのためにussedを初期化
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
    for v in range(N):
        lbs = group[v] # ノードvが所属するグループ
        for w in G[v]: # ノードvから順方向で直接つながっているノードwがノードvとは異なるグループに所属する場合はグループごとの順方向接続を保存する。
            lbt = group[w]
            if lbs == lbt:
                continue
            G0[lbs].add(lbt)
        GP[lbs].append(v)
    return G0, GP