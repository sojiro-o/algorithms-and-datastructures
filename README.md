# かっこいい入力・出力・修飾方法

## 入出力
#### いきなり行列としてinputする時
```.py
[list(map(int,input().split()) for _ in range(high))]
```

#### 複数行に渡る出力する時
```.py
ans = list(hogehoge)
print(*ans, sep = "\n")
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

