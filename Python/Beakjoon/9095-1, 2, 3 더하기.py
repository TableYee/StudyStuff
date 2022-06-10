def calc(n):
    for i in range(4,n+1):
        dp[i] = dp[i-1] + dp[i-2] + dp[i-3]
    return 0

t = int(input())
dp = [0]*12
dp[1] = 1; dp[2] = 2; dp[3] = 4
lst = [int(input()) for i in range(t)]
calc(max(lst))

for i in lst:
    print(dp[i])