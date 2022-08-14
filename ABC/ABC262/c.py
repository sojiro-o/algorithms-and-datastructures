import sys
import itertools

# テスト入力用 readlineの上に配置する
# import io
# _INPUT = u"""\
# 4
# 1 3 2 4
# """
# sys.stdin = io.StringIO(_INPUT)
lines = [s.strip() for s in sys.stdin.readlines()]

N = int(lines[0])
A = list(map(int, lines[1].split()))

num_is_index= 0
pattern2 = 0
for i,num in enumerate(A,1):
    if i == num:
        num_is_index+=1
    elif A[num-1] == i:
        pattern2 += 1

pattern1 = num_is_index*(num_is_index-1) // 2

print(pattern1+pattern2//2)