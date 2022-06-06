from collections import deque
n,k = map(int,input().split())
lst = deque(list(range(1,n+1)))
ans = []

for i in range(n):
    for i in range(k-1):
        lst.append(lst.popleft())
    ans.append(lst.popleft())
print("<",end='')
print(*ans,sep=', ',end='')
print(">",end='')