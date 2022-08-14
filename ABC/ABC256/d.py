import sys

# テスト入力用 readlineのしたに配置する
# import io
# _INPUT = u"""\
# 5
# abcde
# """
# sys.stdin = io.StringIO(_INPUT)


lines = [s.strip() for s in sys.stdin.readlines()]

N = int(lines[0])
LR = []
for lr in lines[1:]:
    LR.append(lr)
    
S = str(lines[1])

print(S[-1])