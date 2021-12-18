# かっこいい入力・出力・修飾方法

## 入出力
#### いきなり行列としてinputする時
```.py
[list(map(int,input().split())) for _ in range(N)]
```
#### 空の頂点隣接リスト
rinsetu= [[] for _ in range(H*W)]

#### 複数行に渡る出力する時
```.py
ans = list(hogehoge)
print(*ans, sep = "\n")
```
#### 入力の高速化
```.py
import sys
input = sys.stdin.readline
```
ただし、インタラクティブシェルでやると壊れる

#### 再帰のエラーはこれを疑え (再帰上限の引き上げ)
```.py
import sys
sys.setrecursionlimit(10 ** 9)
```

#### リストから出力の空白を消す
```.py
"".join(ans)
```


#### 重みを含めた頂点連結リストの作成
```.py
from collections import defaultdict
Tree = defaultdict(lambda: [])

# input data
N = int(input())
for _ in range(N - 1):
    s, t, w = map(int, input().split())
    Tree[s].append((t, w))
    Tree[t].append((s, w))
```


## 修飾
#### 文字の一部を置き換える時
```.py
word = word.replace("前","後")
```
#### 累積和を求める時
```.py
list[i+1] += list[i]
```
#### ある数が奇数かどうか
```.py
if x & 1:
```

## その他
#### 二次元配列のn番目の要素が最大なものを取得したい
max関数のkeyにlambda関数を指定する。
例
```.py
select_one=[[1, 3, 1], [1, 6, 6], [1, 7, 5],[1,2,2],[1,3,3]] 
print(max(select_one, key = lambda x: x[1]))
# 出力: [1, 7, 5]

select_one.index(max(select_one, key = lambda x: x[1]))
# 出力: 2
```

#### 次元配列のn番目の要素で並び替えをしたい
```.py
dictionary = [['なら',3], ['かながわ',4], ['とうきょう',1], ['おおさか',2]]

print(dictionary) # [['なら', 3], ['かながわ', 4], ['とうきょう', 1], ['おおさか', 2]]

sortedDict = sorted(dictionary, key=lambda x: x[1])

print(sortedDict) # [['とうきょう', 1], ['おおさか', 2], ['なら', 3], ['かながわ', 4]]
```

# もう一回やる問題
43 58

# 星4の58以降をもう一回

# 備忘メモ
- スライド最小値


certifi==2019.11.28
chardet==3.0.4
dbus-python==1.2.16
distro-info===0.23ubuntu1
idna==2.8
nose==1.3.7
Pygments==2.3.1
PyGObject==3.36.0
python-apt==2.0.0+ubuntu0.20.4.6
PyYAML==5.3.1
requests==2.22.0
requests-unixsocket==0.2.0
six==1.14.0
unattended-upgrades==0.1
urllib3==1.25.8