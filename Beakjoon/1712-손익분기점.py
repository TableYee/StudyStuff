a,b,c = map(int,input().split())
c-=b

if c <= 0:
    print(-1)
else:
    print(int(a/c) + 1)