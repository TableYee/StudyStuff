from math import sqrt
import sys
input = sys.stdin.readline

def calc(x1,y1,x2,y2,a,b,r):
    dist1 = sqrt(abs(x1 - a)**2 + abs(y1 - b)**2)
    dist2 = sqrt(abs(x2 - a)**2 + abs(y2 - b)**2)
    if dist1 < r and dist2 < r: return 0
    elif dist1 < r and dist2 > r: return 1
    elif dist1 > r and dist2 < r: return 1
    else: return 0

T = int(input())

for i in range(T):
    ans = 0
    x1,y1,x2,y2 = map(int,input().split())
    n = int(input())
    for j in range(n):
        cx,cy,r = map(int,input().split())
        ans += calc(x1,y1,x2,y2,cx,cy,r)
    print(ans)
        