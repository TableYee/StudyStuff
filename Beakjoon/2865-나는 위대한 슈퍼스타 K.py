n,m,k = map(int,input().split())
ans = 0
lst = [list(map(float,input().split())) for i in range(m)]
comp = [0 for i in range(n)]

for _ in range(m):
    for i,j in zip(range(0,n*2,2),range(1,n*2+1,2)):
        if comp[int(lst[_][i])-1] < lst[_][j]:
            comp[int(lst[_][i])-1] = lst[_][j]

for i in range(k):
    ans+=max(comp)
    del comp[comp.index(max(comp))]
print(ans)