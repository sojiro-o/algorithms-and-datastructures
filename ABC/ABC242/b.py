import sys

# テスト入力用 readlineのしたに配置する
# import io
# _INPUT = u"""\
# aba
# """
# sys.stdin = io.StringIO(_INPUT)


lines = [s.strip() for s in sys.stdin.readlines()]

S = list(lines[0])
S.sort()
print(''.join(S))
