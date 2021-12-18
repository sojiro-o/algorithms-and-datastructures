"""
〜segfuncの使い方について〜
update(k, x): k番目の要素をxに更新する
query(l, r): [l, r)（l <= k < r の区間）から値kを取得する
"""
def segfunc(x: int, y: int) -> int:
    "ここで求めたい処理を行う, max(x, y) や x ^ y (排他的論理和) など"
    return max(x, y)

"""
〜単位元の一覧について〜
最小値：float("inf")
最大値：-float("inf")
XOR：0
区間和：0
区間積：1
最大公約数：0
"""
ide_ele = 0 # 初期値（単位元）の設定

class LazySegmentTree:
    # 0 index, init_valに初期配列を格納
    def __init__(self, init_val, segfunc, ide_ele):
        n = len(init_val) # init_valが初期値のリストになる。今回はa = [0] * w、本来的に扱いたい数たちの個数
        self.segfunc = segfunc
        self.ide_ele = ide_ele
        # nより上の数の2の累乗数で一番小さいのがnum
        self.num = 1 << (n - 1).bit_length() # 2**(n - 1).bit_length()  x.bit_length() は 2**(k-1) <= abs(x) < 2**k を満たすk
        self.data = [ide_ele] * 2 * self.num # 最大でもこの数のみ必要 (少し余る)
        self.lazy = [None] * 2 * self.num # 最大でもこの数のみ必要
        for i in range(n):
            self.data[self.num + i] = init_val[i] # 底辺の初期値を入れる。底辺の初期値の数はあくまで「 n 」
        for i in range(self.num - 1, 0, -1): # 上側のノード
            self.data[i] = self.segfunc(self.data[2 * i], self.data[2 * i + 1]) # 下の子に対してself.segfuncを実行をして、親ノードに渡す

# self.dataのself.numまでは2**xで連結する木構造が格納されているが (self.data[0]が一番上の根)、self.dataのself.num+1からは底辺の値

    def gindex(self, l, r): # lからrまでの変数の増加で変更しなくてはならない上流ノードをイテレータとして返してくれる
        l += self.num # 底辺はself.numから始まるのでプラスする
        r += self.num
        lm = l >> (l & -l).bit_length() # ある数の約数の中で2**xの形で表せられるものの中で最大のもの
        rm = r >> (r & -r).bit_length() # 初めて自分より小さい値が入ってくるような覆いかぶさりの値
        # 例: l=3, r=8の場合、
        while l < r: # 返り値は２つ
            if l <= lm:
                yield l
            if r <= rm:
                yield r
            r >>= 1  # 2で割っている
            l >>= 1  # 奇数の上に完全覆いかぶさりは存在せず、2で割り続けて最初に出てくる奇数はそれまでの完全覆いかぶさり
        while l: # 返り値は１つ
            yield l
            l >>= 1

    def propagates(self, *ids): # 以下のupdate、queryを行う度にpropagatesを行い、lazyの値を下に下ろす
        for i in reversed(ids): # 変更しなくてはならない上流ノードから下流へ変更を伝える
            # そのノードのlazyを下へとバトンパスする
            v = self.lazy[i]
            if v is None:
                continue
            self.lazy[2 * i] = v
            self.lazy[2 * i + 1] = v
            self.data[2 * i] = v
            self.data[2 * i + 1] = v
            self.lazy[i] = None

    def update(self, l, r, x): # 底辺のノードが更新されたことによる区間最大値の更新 (+1をする)
        *ids, = self.gindex(l, r)
        self.propagates(*ids) # 指定範囲内のlazyを処理
        l += self.num
        r += self.num
        while l < r:
            if l & 1:
                self.lazy[l] = x
                self.data[l] = x
                l += 1
            if r & 1:
                self.lazy[r - 1] = x
                self.data[r - 1] = x
            r >>= 1
            l >>= 1
        for i in ids:
            self.data[i] = self.segfunc(self.data[2 * i], self.data[2 * i + 1])

    def query(self, l, r): # lからrまでの最大値を取得
        *ids, = self.gindex(l, r)
        self.propagates(*ids)  # 指定範囲内のlazyを処理
        res = self.ide_ele
        l += self.num
        r += self.num
        while l < r:
            if l & 1:
                res = self.segfunc(res, self.data[l])
                l += 1
            if r & 1:
                res = self.segfunc(res, self.data[r - 1])
            l >>= 1
            r >>= 1
        return res

w, n = map(int,input().split()) # 配列の長さ・クエリ数
a = [0] * w
seg = LazySegmentTree(a, segfunc, ide_ele)
for i in range(n):
    l, r = map(int,input().split())
    cnt = seg.query(l - 1, r) # l, r は1 index,rは開区間なのでそのまま利用。0 indexで[l-1,r)のうちの最大値を取得する)
    seg.update(l - 1, r, cnt + 1) # 0 indexで[l-1,r)の区間をその最大値 +1 に書き換える
    print(cnt + 1)