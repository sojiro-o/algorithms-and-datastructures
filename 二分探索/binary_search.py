# is_ok: この関数が条件を満たすかどうかを二分探索
def is_ok(index):
    # 問題によってここの条件を変更する
    if a[index] >= key:
        return True
    else:
        return False

# a = list()
# left, right = -1, len(a)

def meguru_bisect(left, right):
    # リストの右に行けば条件を満たすという前提
    # left以下、条件を満たさない集合
    # right以上、条件を満たす集合
    while right - left > 1:
        mid = (right + left) // 2
        if is_ok(mid): # まだまだ小さくできる
            # ここより下のrightとleftを変換すると条件を満たす一番大きなindexを取得できる
            right = mid
        else:
            left = mid # 今のよりはmid小さくできない
    return right # 条件を満たす一番小さなindex


def meguru_bisect(left, right):
    # リストの左に行けば条件を満たすという前提
    # left以下、条件を満たす合
    # right以上、条件を満たさない集合
    while right - left > 1:
        mid = (right + left) // 2
        if is_ok(mid): # まだまだ小さくできる
            # ここより下のrightとleftを変換すると条件を満たす一番大きなindexを取得できる
            left = mid
        else:
            right = mid # 今のよりはmid小さくできない
    return left # 条件を満たす一番大きなindex






# 0からlまでの中で条件を満たす数を返す
# 例　print(meguru_bisect(l,0))

# 範囲に正解がふくまれていない可能性がある場合
# https://atcoder.jp/contests/abc231/tasks/abc231_c
N, Q = map(int,input().split())
A = list(map(int,input().split()))
A.sort()

# len(A) = N

for _ in range(Q):
    x = int(input())
    # right - leftの差が2の所でストップするのでindexは-1から考える
    right = lem(A) # 扱う対象の最大インデックスより一つ大きい値にすることで、そもそもA[N]でも駄目な場合も一緒に考えることができる。
    left = -1
    while right - left > 1:
        mid = (right + left) // 2
        if A[mid] < x: # まだまだ大きくできる
            left = mid
        else:
            right = mid
    print(N-right)