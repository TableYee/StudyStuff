n,m = map(int,input().split())
lst = [i for i in range(1,n+1)]

for i in range(m):
    b1,b2 = map(int,input().split())
    b1-=1; b2-=1
    lst[b1],lst[b2] = lst[b2], lst[b1]

print(*lst)