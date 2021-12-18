# is_ok: この関数が条件を満たすかどうかを二分探索

def meguru_bisect(right, left):
    while right - left > 1:
        mid = (right + left) // 2
        if is_ok(mid) >= k + 1: # まだまだ大きくできる
            left = mid
        else:
            right = mid # 小さくしなければいけない
    return ok

# 0からlまでの中で条件を満たす数を返す
# 例　print(meguru_bisect(l,0))

# 範囲に正解がふくまれていない可能性がある場合
# https://atcoder.jp/contests/abc231/tasks/abc231_c
N, Q = map(int,input().split())
A = list(map(int,input().split()))
A.sort()

for _ in range(Q):
    x = int(input())
    if x <= A[0]:
        # right - leftの差が2の所でストップするので、そもそもA[0]でも駄目な場合は別に考える。
        print(N)
    else:
        right = N # 扱う対象の最大インデックスより一つ大きい値にすることで、そもそもA[N]でも駄目な場合も一緒に考えることができる。
        left = 0
        while right - left > 1:
            mid = (right + left) // 2
            if A[mid] < x: # まだまだ大きくできる
                left = mid
            else:
                right = mid
        print(N-right)