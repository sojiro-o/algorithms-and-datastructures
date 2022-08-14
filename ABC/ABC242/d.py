import sys

# テスト入力用 readlineのしたに配置する
import io
_INPUT = u"""\
CBBAACCCCC
5
57530144230160008 659279164847814847
29622990657296329 861239705300265164
509705228051901259 994708708957785197
176678501072691541 655134104344481648
827291290937314275 407121144297426665
"""
sys.stdin = io.StringIO(_INPUT)


lines = [s.strip() for s in sys.stdin.readlines()]

S = str(lines[0])
Q = int(lines[1])

def abc_012(start):
    if start == "A":
        start_num = 0
    elif start == "B":
        start_num = 1
    else:
        start_num = 2
    return start_num

for line in lines[2:]:
    t,k = map(int, line.split())
    k -= 1
    if t == 0:
        print(S[k])
        continue
    operation = []
    for _ in range(t):
        if k%2 == 0:
            operation.append(0)
            k = k // 2
        else:
            operation.append(1)
            k = k // 2
    operation_num = len(operation) + sum(operation)
    start = S[k] # 何番目かは0-based
    # print(start, operation_num)
    start_num = abc_012(start)
    ans_num = (start_num+operation_num) % 3
    # print(ans_num)
    ans = "ABC"[ans_num]
    print(ans)