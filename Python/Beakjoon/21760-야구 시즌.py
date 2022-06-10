import sys
input = sys.stdin.readline
t = int(input())

for _ in range(t):
    leage,team,k,d = map(int,input().split())

    b=1
    a = b*k
    diff = team**2*(leage*(leage-1)/2)*b
    same = leage*a*(team*(team-1)/2)
    ans = d//(diff+same) * (diff+same)

    if diff + same > d:
        print(-1)
    else: print(int(ans))

