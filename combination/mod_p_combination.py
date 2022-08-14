class Combination():

    def __init__(self, prime=10**9+7, max_num=10**6):
        '''
        prime: mod prime (素数) におけるnCrを算出する
        max_num: 高速に演算するためにメモを作る. nより大きい数であればよい
        '''        
        # max_num nより十分に大きい数を設定
        fact = [1, 1]
        factinv = [1, 1]
        inv = [0, 1]
        
        for i in range(2, max_num + 1):
            fact.append((fact[-1] * i) % prime)
            inv.append((-inv[prime % i] * (prime // i)) % prime)
            factinv.append((factinv[-1] * inv[-1]) % prime)

        self.prime = prime
        self.fact = fact
        self.factinv = factinv
        self.inv = inv

    def cmb(self, n, r):
        if (r < 0) or (n < r):
            return 0
        r = min(r, n-r)
        return self.fact[n] * self.factinv[r] * self.factinv[n-r] % self.prime

# 使用例  
cmb = Combination(10**9+7,100) # primeとmax_numを指定
print(cmb.cmb(4,2)) # _4C_2