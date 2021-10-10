n = int(input())
arr = [[0]]
for i in range(n):
    arr.append([0]+list(map(int,input().split())))
dp = [[0] for i in range(n+1)]
dp[1]+=[arr[1][1]]

for i in range(2,n+1):
    cnt = 0
    chk = True
    for j in range(1,len(dp[i-1])):
        cnt+=1
        print(arr[i-1])
        if cnt > (len(arr[i-1])+1)//2 and chk and i > 3:
            cnt=2
            chk = False
        print(cnt,i,j)
        dp[i] += [dp[i-1][j]+arr[i][cnt],dp[i-1][j]+arr[i][cnt+1]]
        print(dp,i,j)

print(max(dp[-1]))