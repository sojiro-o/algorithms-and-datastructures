import sys

# テスト入力用 readlineの上に配置する
# import io
# _INPUT = u"""\
# abbaac
# abbbbaaac
# """
# sys.stdin = io.StringIO(_INPUT)

lines = [s.strip() for s in sys.stdin.readlines()]
S = str(lines[0])
T = str(lines[1])

def contents_num(s):
    past_alphabet = ""
    past_num = 0
    contents = [] # 登場したら加える
    nums = [] # 退場したら加える
    for i, alphabet in enumerate(s):
        if alphabet != past_alphabet:
            contents.append(alphabet) # 登場したので加える
            past_alphabet = alphabet # 更新
            if past_num != 0:
                nums.append(past_num) # 退場したので加える
            past_num = 1 # 更新

        elif alphabet == past_alphabet:
            past_num += 1
        
        # 上の処理の後
        if i == len(s)-1:
            nums.append(past_num)

    return contents, nums

S_contents, S_num = contents_num(S)
T_contents, T_num = contents_num(T)

if S_contents != T_contents:
    print("No")
    exit()

for s,t in zip(S_num, T_num):
    if s == t:
        continue
    elif s > t:
        print("No")
        exit()
    elif s < t:
        if s >= 2:
            continue
        else:
            print("No")
            exit()

print("Yes")

