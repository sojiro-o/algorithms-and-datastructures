def bellman_ford(edges, s, N):
    '''
    edges ... (cost,from,to)を各要素に持つリスト
    s...始点ノード
    N...頂点数

    return
    ----------
    D ... 各点までの最短距離
    P ... 最短経路木における親
    '''
    P = [None] * N
    inf = float('inf')
    D = [inf] * N
    D[s] = 0
    for n in range(N):  # N-1回で十分だけど、N回目にもアップデートがあったらnegative loopを検出できる
        update = False  # 早期終了用
        for c, ot, to in edges:
            if D[ot] != inf and D[to] > D[ot] + c:
                update = True
                D[to] = D[ot] + c
                P[to] = ot
        if not update:
            break  # 早期終了
        if n == len(edges) - 1:
            print(-1)  # 負の閉路が存在するということはそのように並ぶことはできないということ
            exit()
            raise ValueError('NegativeCycleError')
    return D, P