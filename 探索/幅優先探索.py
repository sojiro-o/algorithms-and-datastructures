from collections import deque

n, m = map(int, input().split())

graph = [[] for _ in range(n+1)]

for i in range(m):
    a, b = map(int, input().split())
    graph[a].append(b)
    graph[b].append(a)

dist = [-1] * (n+1)
dist[0] = 0
dist[1] = 0

d = deque()
d.append(1)

while d:
    v = d.popleft()
    for i in graph[v]:
        if dist[i] != -1:
            continue
        dist[i] = dist[v] + 1
        d.append(i)

ans = dist[1:]
print(*ans, sep="\n")















# 例


while que:
    x, y = que.popleft() # キューから取り出し

    # 現在位置から上下左右に探索
    for i, j in d:
        # 前提条件
        if x+i >= R or x+i < 0 or y+j >= C or y+j < 0: # 範囲外
            continue
        if maze[x+i][y+j] == '#': # 壁
            continue
        
        # キューの追加の時に既に訪問したかの条件を入れるのもよい
        if dist[x+i][y+j] != 10**4: # すでに最小手数確定済み
            continue

        dist[x+i][y+j] = dist[x][y] + 1

        que.append([x+i, y+j]) # 次のマスをキューに格納

print(dist[gx][gy])