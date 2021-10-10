n = int(input())
arr = list(map(int,input().split()))
lst = []
cnt = 0

for i in range(n):
    if arr[i] == i+1:
        continue
    if i > arr.index(i+1):
        lst.append([arr.index(i+1)+1,i+1])
        if arr.index(i+1) == 0:
            arr = arr[:arr.index(i+1)] + arr[i::-1] + arr[i+1:]
        elif i+1 == n:
            arr = arr[:arr.index(i+1)] + arr[:arr.index(i+1)-1:-1] + arr[i+1:]
        else:
            arr = arr[:arr.index(i+1)] + arr[i:arr.index(i+1)-1:-1] + arr[i+1:]
        print(arr+"1")
    else:
        lst.append([i+1,arr.index(i+1)+1])
        if arr.index(i+1) == 0:
            arr = arr[:i] + arr[arr.index(i+1)::-1] + arr[arr.index(i+1)+1:]
        elif i == n:
            arr = arr[:i] + arr[arr.index(i+1)::-1] + arr[arr.index(i+1)+1:]
        else:
            arr = arr[:i] + arr[arr.index(i+1):i-1:-1] + arr[arr.index(i+1)+1:]
        print(arr)
    cnt += 1

print(cnt)
for i,j in lst:
    print(i,j)
"""
a=[3,2,1,4,5]
i,j=1,4
a=a[:i]+a[:i-1:-1]+a[j+1:]

print(a)"""