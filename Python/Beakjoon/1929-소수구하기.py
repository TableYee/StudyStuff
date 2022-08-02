m,n = map(int,input().split())
lst = [1]*(n+1)
lst[0] = 0
lst[1] = 0

for i in range(2,n+1):
    for j in range(i*2,n+1,i):
        lst[j] = 0

for i in range(m,n+1):
    if lst[i]:
        print(i)