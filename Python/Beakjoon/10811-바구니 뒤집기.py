n,m = map(int,input().split())
lst = [i for i in range(1,n+1)]

for i in  range(m):
    s,e = map(int,input().split())
    lst[s-1:e] = reversed(lst[s-1:e])
print(*lst)