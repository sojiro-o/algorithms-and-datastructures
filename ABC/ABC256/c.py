import sys


# テスト入力用 readlineのしたに配置する
# import io
# _INPUT = u"""\
# 20 25 30 22 29 24
# """
# sys.stdin = io.StringIO(_INPUT)


lines = [s.strip() for s in sys.stdin.readlines()]

h_1, h_2, h_3, w_1, w_2, w_3 = map(int, lines[0].split())

# for文で3変数を固定する
count = 0
for a in range(1, min(h_1-2, w_1-2) +1):
    for b in range(1, min(h_1-1-a, w_2-2) +1):
        c = h_1-a-b # cが決定する
        if c <= 0:
            continue
        for d in range(1, min(h_2-2, w_1-1-a) +1):
            # すべての変数が決定する
            g = w_1-a-d
            for e in range(1, min(h_2-1-d, w_2-1-b) +1):
                f = h_2-d-e
                if f <= 0:
                    continue
                h = w_2-b-e
                i = w_3-c-f
                if h<=0 or i<=0:
                    continue
                if h + i == h_3 - g:
                    count += 1
                

print(count)
