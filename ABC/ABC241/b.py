import sys

# テスト入力用 readlineの上に配置する
import io
_INPUT = u"""\
3 2
1 1 3
3 1
"""
sys.stdin = io.StringIO(_INPUT)


lines = [s.strip() for s in sys.stdin.readlines()]

N, M = map(int, lines[0].split())
a_list = list(map(int, lines[1].split()))
b_list = list(map(int, lines[2].split()))
 
for b in b_list:
    try:
        a_list.remove(b)
    except:
        exit(print("No"))
print("Yes")