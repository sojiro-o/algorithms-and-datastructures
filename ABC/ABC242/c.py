import sys

# テスト入力用 readlineのしたに配置する
# import io
# _INPUT = u"""\
# 1000000
# """
# sys.stdin = io.StringIO(_INPUT)


lines = [s.strip() for s in sys.stdin.readlines()]

N = int(lines[0])
dp = [[0]*9 for _ in range(N)]
dp[0] = [1]*9

for i in range(1,N):
    dp[i][0] = (dp[i-1][0] + dp[i-1][1]) % 998244353
    dp[i][1] = (dp[i-1][0] + dp[i-1][1] + dp[i-1][2]) % 998244353
    dp[i][2] = (dp[i-1][1] + dp[i-1][2] + dp[i-1][3]) % 998244353
    dp[i][3] = (dp[i-1][2] + dp[i-1][3] + dp[i-1][4]) % 998244353
    dp[i][4] = (dp[i-1][3] + dp[i-1][4] + dp[i-1][5]) % 998244353
    dp[i][5] = (dp[i-1][4] + dp[i-1][5] + dp[i-1][6]) % 998244353
    dp[i][6] = (dp[i-1][5] + dp[i-1][6] + dp[i-1][7]) % 998244353
    dp[i][7] = (dp[i-1][6] + dp[i-1][7] + dp[i-1][8]) % 998244353
    dp[i][8] = (dp[i-1][7] + dp[i-1][8]) % 998244353

print(sum(dp[N-1])%998244353)