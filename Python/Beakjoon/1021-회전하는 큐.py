from math import ceil
from collections import deque

n,m = map(int,input().split())
nums = list(map(int,input().split()))
que = deque([i for i in range(1,n+1)])
ans = 0

for i in nums:
    med = ceil(len(que)/2)
    if que.index(i)+1 <= med:
        while True:
            if que[0] == i:
                que.popleft()
                break
            que.append(que.popleft())
            ans+=1
    else:
        while True:
            if que[0] == i:
                que.popleft()
                break
            que.appendleft(que.pop())
            ans+=1
print(ans)
