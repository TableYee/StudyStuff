from math import ceil
n,m,k = map(int,input().split())
arr = [[0 for i in range(m)] for j in range(n)]
arr[0][0] = 1
if k != 0:
    pointX,pointY = k%m-1 if k%m != 0 else m-1, ceil(k/m)-1 if m != 1 else 0
else: pointX, pointY = 0, 0

#to K
for y in range(pointY+1):
    for x in range(pointX+1):
        if x+1 <= pointX:
            arr[y][x+1] += arr[y][x]
        if y+1 <= pointY:
            arr[y+1][x] += arr[y][x]
ans1 = arr[pointY][pointX]
arr[pointY][pointX] = 1

#from K to (m,n)
for y in range(pointY,n):
    for x in range(pointX,m):
        if x+1 < m:
            arr[y][x+1] += arr[y][x]
        if y+1 < n:
            arr[y+1][x] += arr[y][x]
print(ans1*arr[n-1][m-1])
"""
1 2 3 4 5 
6 7 8 9 10 
11 12 13 14 15 
16 17 18 19 20 5
21 22 23 24 25 
"""