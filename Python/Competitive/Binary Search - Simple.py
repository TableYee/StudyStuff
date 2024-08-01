n = int(input())
lst = list(map(int,input().split()))
hi,lo = len(lst)-1, 0

while True:
    mid = (lo+hi) // 2
    print(lo,mid,hi, lst[mid])

    if hi < lo:
        print(mid+1)
        break
    

    if lst[mid] > n:
        hi = mid-1
    elif lst[mid] < n: 
        lo = mid+1
    else:
        print(mid)
        break

