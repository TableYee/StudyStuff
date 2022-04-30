n = int(input())
stairs = [int(input()) for i in range(n)]
stairs = [0]+stairs
dp = [0] * (n+20)

if n == 1:
    print(stairs[1])
    quit()
dp[1] = stairs[1]
dp[2] = stairs[1] + stairs[2]

for i in range(3,n+1):
    dp[i] = stairs[i] + max(dp[i-2],stairs[i-1] + dp[i-3])
    
dp = dp[::-1]
for i in range(len(dp)):
    if dp[i] != 0:
        print(dp[i])
        break
