def twoPointer(hi,lo,num):
    while True:
        if hi==lo:
            return False
        
        if arr[hi]+arr[lo] < num:
            lo+=1
        elif arr[hi]+arr[lo] > num:
            hi-=1
        else:
            return True

n = int(input())
lst = list(map(int,input().split()))
lst.sort()
ans = 0

for i in range(0,n):
    arr = lst[:i]+lst[i+1:]
    if twoPointer(n-2,0,lst[i]): 
        ans+=1
print(ans)