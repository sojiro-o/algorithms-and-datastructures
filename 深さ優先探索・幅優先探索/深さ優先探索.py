# 再帰関数を使う場合
def dfs(now):
    for i in path[now]:
        #path[now] (nowと隣り合うノード)から複数のノードに移動できたとしても、先に１つ目の移動先をすべて見終わるまで次のforに行かないので深さ優先になる
        if is_calculated[i] == False:
            #訪問済みかどうか
            counter[i]+=counter[now] # 何かしらの処理
            is_calculated[i]=True # 訪問済みにする
            dfs(i) # 最後に再帰
    # 帰りがけ処理

# メモリを使用する場合
from collections import deque#listより速いスタックやキューで使うデータ形式
def dfs_memory(start_node):
    
    s = deque([]) #計算すべき始点となるノードを管理し、ここに値がある限り処理を続けます。
    s.append(start_node) #とりあえず頂点1からはじめるので、sに頂点1を追加します。
    while not len(s) == 0:
        now = s.pop() #FILOなのでスタックとして使う　now = s.popleft() とすると幅優先探索
        for next in path[now]:#現在のノードから移動可能なノードを取り出します。複数あれば複数処理が必要です。
            if is_calculated[next]:
                continue
            s.append(next)#次回以降に始点とするべきノードをsに追加します。
            is_calculated[next] = True#計算済みにする
            counter[next] += counter[now]#カウンターを加算（直前のノードからの累積和）
    
    
    return