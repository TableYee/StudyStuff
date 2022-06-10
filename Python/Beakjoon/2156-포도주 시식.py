n = int(input())
wines = [int(input()) for i in range(n)]
dp = {}
temp = {}
for i in range(n):
    dp[wines[i]] = [wines[i]]
print(dp)

for i in range(n):
    for key,value in dp.items():
        if wines[i] in value:
            continue
        cur = wines[i] + key
        temp[cur] = value + [wines[i]]
    dp |= temp
print(dp)
print(max(dp.keys()))