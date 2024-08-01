n = int(input())
lst = list(map(int,input().split()))
lst.sort()

ans = [0,0]
minAcidity = 10**10
lo,hi = 0,n-1
while True:
    if hi==lo:
        print(lst[ans[0]],lst[ans[1]])
        break

    acidity = lst[hi]+lst[lo]
    if abs(acidity) < minAcidity:
        minAcidity = abs(acidity)
        ans[0] = lo
        ans[1] = hi
    
    if 0 < acidity:
        hi-=1
    elif 0 > acidity:
        lo+=1
    else:
        print(lst[lo],lst[hi])
        break
