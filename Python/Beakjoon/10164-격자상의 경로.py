from re import X


n,m,k = map(int,input().split())
arr = [[0 for i in range(m)] for j in range(n)]
arr[0][0] = 1
print(k//m,k%m-1)
for y in range(k//m):
    for x in range(k%m-1):
        if x+1 < len(arr[y]):
            arr[y][x+1] += arr[y][x]
        if y+1 < len(arr):
            arr[y+1][x] += arr[y][x]

for y in range(k//m,n):
    for x in range(k%m-1,m):
        if x+1 < len(arr[y]):
            arr[y][x+1] += arr[y][x]
        if y+1 < len(arr):
            arr[y+1][x] += arr[y][x]
print(arr)