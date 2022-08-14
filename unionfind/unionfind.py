# ランク無し実装
# リストのインデックスがノード番号に相当する。リストの要素が親ノード番号に相当する。
# 最初は各要素はどこのグループにも属していないので自分自身が親になります。要素数をNとすると[i for i in range(N+1)]となる (1 based)
def find(x):
    # 親が自分自身のノードまで遡る
    if par[x] == x:
        return x
    else:
        par[x] = find(par[x])
        return par[x]

def same(x, y):
    return find(x) == find(y)

def unite(x, y):
    # 元のノード番号の大小で親子関係を決めてしまう
    x = find(x)
    y = find(y)
    if x == y:
        return 0
    if x < y:
        x, y = y, x
    par[x] = y