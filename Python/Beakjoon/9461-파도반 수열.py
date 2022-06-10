def calc(n):
    for i in range(4,n+1):
        dp[i] = dp[i-1] + dp[i-5]
    return 0

t = int(input())
dp = [0]*101
dp[0] = 1; dp[1] = 1; dp[2] = 1; dp[3] = 2; dp[4] = 2;

for i in range(t):
    n = int(input())
    if dp[n] != 0:
        print(dp[n-1])
    else:
        calc(n)
        print(dp[n-1])
