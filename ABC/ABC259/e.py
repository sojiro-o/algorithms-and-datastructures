import sys

# テスト入力用 readlineの上に配置する
# import io
# _INPUT = u"""\
# 1
# 1
# 998244353 1000000000
# """
# sys.stdin = io.StringIO(_INPUT)
lines = [s.strip() for s in sys.stdin.readlines()]

N = int(lines[0])
prime_factors = set()
prime_factors_num = []
point = 1

for _ in range(N):
    M = int(lines[point])
    d = {}
    for line in lines[point+1:point+1+M]:
        p, e = map(int, line.split())
        prime_factors.add(p)
        d[p] = e
    prime_factors_num.append(d)
    point += (1+M)

# print(prime_factors)
# print(prime_factors_num)

# prime_factors_numをリストにする
pfn_lists = []
for pfn in prime_factors_num:
    pfn_keys = pfn.keys()
    pfn_list = []
    for prime_factor in prime_factors:
        if prime_factor in pfn_keys:
            pfn_list.append(pfn[prime_factor])
        else:
            pfn_list.append(0)
    pfn_lists.append(pfn_list)

# print(pfn_lists)

if N==1:
    print(1)
    exit()

# 各因数の指数の唯一の最大値を検索する. ない場合は0とする
max_gyo_list = [] # 同じ行に唯一の指数最大値を取るものが存在する場合への対策
for i in range(len(pfn_lists[0])):
    pfn = [x[i] for x in pfn_lists]
    pfn_sort = sorted(pfn)
    if pfn_sort[-1] != pfn_sort[-2]:
        # 指数が唯一の最大値の場合
        max_gyo_list.append(pfn.index(pfn_sort[-1]))

ans = min(len(set(max_gyo_list))+1, N)
print(ans)
