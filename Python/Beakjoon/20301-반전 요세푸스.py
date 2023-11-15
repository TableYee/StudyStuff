from collections import deque
N,K,M = map(int,input().split())
queue = deque(range(1,N+1))

for i in range(M):
    for j in range(K-1):
        queue.append(queue.popleft())
    print(queue.popleft())
for i in range(N-M):
    for j in range(K):
        queue.appendleft(queue.pop())
    print(queue.popleft())