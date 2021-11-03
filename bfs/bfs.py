# 木の直径を求める
def bfs(Tree, n_V, s):
    '''
    指定した点sからの単一始点で各点までの距離を返す。
    n_Vは頂点の数
    Treeはdefault dictで、valueには(隣接ノード,そこまでのコスト)がリスト形式で格納されているとする。
    '''
    INF = 10**9
    Dists = [INF] * n_V  # 距離の初期化 #こいつを更新して返すことにする
    is_visited = [False] * n_V
    is_visited[s] = True
    que = deque([(s, 0)])  # (ノード番号,そこまでたどり着くためのコスト)
    while que:
        cur, cost = que.popleft()
        Dists[cur] = cost
        for nx_node, nx_cost in Tree[cur]:
            if is_visited[nx_node]:
                continue
            que.append((nx_node, nx_cost + cost))
            is_visited[nx_node] = True

    return Dists