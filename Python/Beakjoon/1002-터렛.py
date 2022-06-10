from math import sqrt

def dis1(dist,r1,r2):
    if dist + r1 < r2 or dist + r2 < r1 or dist > r1+r2:
        return 0
    elif dist == r1+r2 or dist + r1 == r2 or dist + r2 == r1:
        return 1
    elif dist < r1+r2:
        return 2
    return -1

T = int(input())
for _ in range(T):
    x1,y1,r1,x2,y2,r2 = map(int, input().split())
    
    if x1 == x2 and y1 == y2 and r1 == r2:
        print(-1)
        continue
    elif x1 == x2 and y1 == y2:
        print(0)
        continue
    dist = sqrt(abs(x1-x2)**2 + abs(y1-y2)**2)
    print(dis1(dist,r1,r2))