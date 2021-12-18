import bisect

B = [4,1,6,2,8,5,7,3]
N = len(B)
L = [0]

L[0] = B[0]
length = 1 # 1 base index
last_index = 0

for i in range(1,N):
    if L[length-1] < B[i]:
        L.append(B[i])
        length += 1
        last_index = i
    else:
        mutate_index = bisect.bisect_left(L, B[i])
        L[mutate_index] = B[i]

print(len(L))        

# 復元
# リストBは結果の配列ではなく、B[i]= i個連続する時の最小の値となっている
ans_array = [B[last_index]]
B_cut = B[:last_index]
base = B[last_index]
for b in reversed(B_cut):
    if b < base:
        ans_array.append(b)
        base = b
ans_array.reverse()
print(ans_array)


