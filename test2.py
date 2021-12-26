import io
import sys

_INPUT = u"""\
5 5
.....
.....
.....
.....
.....
"""
if __file__ == "test2.py":
    sys.stdin = io.StringIO(_INPUT)

lines = [s.strip() for s in sys.stdin.readlines()]



h, w = map(int, lines[0].split())
s = [list(l) for l in lines[1:]]


count_list = []
is_already = []
route_list = [] # 立ち止まるまでの移動方法

def dfs(now,count,route):
    print(type(route))
    # nowは今の座標, countは"これまで"通ってきた数, routeはこれまで通って来た経路[[i,j],...]
    if now in is_already:
        return 0
    is_already.append(now)
    i, j = now

    if (i>=h or j>=w) or s[i][j]=="#":
        count_list.append(count)
        route_list.append(route)
        return 0

    dfs([i+1,j],count+1,route+[[i+1,j]]) # routeという関数の引数としてのリストとは独立で更新させる
    dfs([i,j+1],count+1,route+[[i,j+1]]) #  確認のため#や範囲外へ出てしまった時の座標を確認する
    
dfs([0,0],1,[])
    
print(max(count_list))
print(route_list)
print(len(route_list))