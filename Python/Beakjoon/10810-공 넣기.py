n,m = map(int,input().split())
lst = [0]*n

for i in range(m):
    s,e,k = map(int,input().split())
    for _ in range(s-1,e):
        lst[_] = k

print(*lst)