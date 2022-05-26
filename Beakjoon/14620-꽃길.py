import copy
def plant(x,y):
    global chklst
    if chklst[y][x] == 1 or chklst[y-1][x] == 1 or chklst[y+1][x] == 1 or chklst[y][x+1] == 1 or chklst[y][x-1] == 1:
        return 0
    chklst[y][x],chklst[y-1][x],chklst[y+1][x],chklst[y][x+1],chklst[y][x-1] = 1,1,1,1,1
    return 1
def money(x,y):
    return sum([flower[y][x],flower[y-1][x],flower[y+1][x],flower[y][x+1],flower[y][x-1]])

n = int(input())
flower = [list(map(int,input().split())) for i in range(n)]
chklst = [[0 for j in range(n)] for i in range(n)]
ans = 10**20

for i in range(1,n-1):
    for j in range(1,n-1):
        default = 0
        chklst = [[0 for j in range(n)] for i in range(n)]

        if plant(j,i) == 0:
            continue
        else:
            default += money(j,i)
        beflst = copy.deepcopy(chklst)
        befdefault = default

        for i1 in range(1,n-1):
            for j1 in range(1,n-1):
                chklst = copy.deepcopy(beflst)
                default = befdefault
                if plant(j1,i1) == 0:
                    continue
                else:
                    default += money(j1,i1)
                for i2 in range(1,n-1):
                    for j2 in range(1,n-1):
                        if chklst[i2][j2] != 1 and chklst[i2-1][j2] != 1 and chklst[i2+1][j2] != 1 and chklst[i2][j2+1] != 1 and chklst[i2][j2-1] != 1:
                            ans = min(default + money(j2,i2),ans)
print(ans)
"""
6
1 0 1 1 0 1        
0 0 0 0 0 0
1 0 1 1 0 1
1 1 1 1 0 1
1 1 1 0 0 0
1 1 1 1 0 1
"""