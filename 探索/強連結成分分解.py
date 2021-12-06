import sys
input = sys.stdin.readline

class SCC:
    def __init__(self, n):
        self.n = n
        self.graph = [[] for _ in range(n)] # 矢印の向きの隣接リストの作成
        self.rev_graph = [[] for _ in range(n)] # 矢印逆向きの隣接リストの作成
        self.labels = [-1] * n
        self.lb_cnt = 0

    def add_edge(self, v, nxt_v):
        # 矢印の向きのグラフと逆向きのグラフを作る
        self.graph[v].append(nxt_v) 
        self.rev_graph[nxt_v].append(v)

    def build(self):
        self.post_order = []
        self.used = [False] * self.n
        for v in range(self.n):
            if not self.used[v]:
                self._dfs(v)
        for v in reversed(self.post_order):
            if self.labels[v] == -1:
                self._rev_dfs(v)
                self.lb_cnt += 1

    def _dfs(self, v): # 関数内のみで使う場合_から始める
        stack = [v, 0] # ある頂点とそれに隣接する頂点の番号
        while stack:
            v, idx = stack[-2:]
            # 大切な分岐 訪問済みであり探索済みであったということ
            if (idx==0) and (self.used[v]): #隣接頂点番号がゼロで探索済みの場合 = その頂点からはどこにも行けない場合
                stack.pop() # 辺の番号を消す (.pop()は末尾) # 下の分岐でもスタックから消されるが、ここで消しておかないと再び巡ってしまう
                stack.pop() # 辺のIDを消す
            else:
                self.used[v] = True # 探索済みにする
                if idx < len(self.graph[v]): # 隣接頂点番号 (頂点vが主役の)がvから出るエッジ数未満の時 (存在している)
                    stack[-1] += 1 # 隣接頂点番号に１を追加する
                    stack.append(self.graph[v][idx]) # その隣接している頂点を追加する (0オリジン、1を追加する前の番号を追加している)
                    stack.append(0) # 隣接番号0を入れる
                else:
                    stack.pop() # 隣接頂点番号=0であり探索前もここで処理される
                    self.post_order.append(stack.pop())

    def _rev_dfs(self, v):
        stack = [v]
        self.labels[v] = self.lb_cnt
        while stack:
            v = stack.pop()
            for nxt_v in self.rev_graph[v]:
                if self.labels[nxt_v] != -1:
                    continue
                stack.append(nxt_v)
                self.labels[nxt_v] = self.lb_cnt

    def construct(self):
        self.dag = [[] for i in range(self.lb_cnt)]
        self.groups = [[] for i in range(self.lb_cnt)]
        for v, lb in enumerate(self.labels):
            for nxt_v in self.graph[v]:
                nxt_lb = self.labels[nxt_v]
                if lb == nxt_lb:
                    continue
                self.dag[lb].append(nxt_lb)
            self.groups[lb].append(v)
        return self.dag, self.groups

n, m = map(int, input().split())
graph = [list(map(int,input().split())) for _ in range(m)]
scc = SCC(n)

for u, v in graph:
    scc.add_edge(u - 1, v - 1)
scc.build()
_,elems = scc.construct()

ans = 0
for i in range(len(elems)):
    ans += len(elems[i]) * (len(elems[i]) - 1) // 2

print(ans)