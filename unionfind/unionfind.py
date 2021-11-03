# リストのインデックスがノード番号に相当する。リストの要素が親ノード番号に相当する。
# 扱うノードの大きさのリストを渡す。0オリジンなので、扱うノードが1オリジンの場合は[i for i in range(N+1)]とする
def find(x):
    if par[x] == x:
        return x
    else:
        par[x] = find(par[x])
        return par[x]

def same(x, y):
    return find(x) == find(y)

def unite(x, y):
    x = find(x)
    y = find(y)
    if x == y:
        return 0
    if x < y:
        x, y = y, x
    par[x] = y

# 使用例

