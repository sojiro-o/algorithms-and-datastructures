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