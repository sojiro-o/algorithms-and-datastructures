import sys

# テスト入力用 readlineの上に配置する
# import io
# _INPUT = u"""\
# 11
# a
# a
# a
# a
# a
# a
# a
# a
# a
# a
# a
# """
# sys.stdin = io.StringIO(_INPUT)

lines = [s.strip() for s in sys.stdin.readlines()]

N = int(lines[0])

word_set = set()
word_dict = {}

for s in lines[1:]:
    if not s in word_set:
        word_set.add(s)
        word_dict[s] = 0
        print(s)
    else: # 既出の場合
        word_dict[s] += 1
        print(s+"({})".format(str(word_dict[s])))