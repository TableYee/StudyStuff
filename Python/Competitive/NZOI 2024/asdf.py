n = int(input())
lst = list(range(1,n+1))
mid = n//2

if n%2==0:
    for i in range(n):
        if i%2==0:
            print(n, end=' ')
            n-=1
        else:
            print(mid,end=' ')
            mid-=1
else:
    print(1,end=' ')
    for i in range(n):        
        if i%2==0:
            print(n, end=' ')
            n-=1
        else:
            print(mid,end=' ')
            mid-=1
        
    