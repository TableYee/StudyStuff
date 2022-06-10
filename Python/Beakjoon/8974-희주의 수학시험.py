a,b = map(int,input().split())
lst = [j for j in range(1,b) for i in range(j)]
if b == 1:
    print(1)
else:
    print(sum(lst[a-1:b]))
