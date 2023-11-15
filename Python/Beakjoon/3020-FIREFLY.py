n,h = map(int,input().split())
up,down = []*h,[]*h

for i in range(n):
    if i % 2 == 0:
        up[int(input())] += 1
    else:
        down[h-int(input())] += 1

for i in range(h-1,0,-1):
    up[i-1] += up[i]
    down[i-1] += up[i]

