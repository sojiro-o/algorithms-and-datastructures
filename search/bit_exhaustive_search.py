from itertools import combinations
def bit_search(A):
    '''
    入力リスト 0 base index
    出力リスト index: 使用した要素の個数, content: 取りうる値のリスト    1 base index
    '''
    bitlist = [[] for _ in range(len(A)+1)] 
    for k in range(len(A)+1):
        for comb_A in combinations(A, k):
            # comb_Aは要素数kのタプル
            bitlist[k].append(sum(comb_A)) # 何かしらの処理 今回は和を取った
    
    return semilist







# 若しくは
from itertools import product

def bit_search(A: list, l: int):
    "配列, 配列の長さ"
    num_list = [[] for _ in range(l + 1)] # 0 ~ lまでのl + 1個の配列を用意する
    for i in product([0, 1], repeat = l):
        num = 0
        for j in range(l):
            if i[j] == 1:
                num += A[j]
        num_list[i.count(1)].append(num)
    
    # 昇順にする
    for i in range(len(num_list)):
        num_list[i].sort()
    
    return num_list