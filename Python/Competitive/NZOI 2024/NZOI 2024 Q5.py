from collections import deque
import sys
input = sys.stdin.readline
def SearchTrout(p):
    que = deque()
    que.append([p,0])
    ans = 0
    visited = []
    while que:
        curPos,curLength = que.pop()
        if curPos in visited:
            continue 
        for i in trouts[curPos]:
            if i >= curLength:
                ans+=1
        visited.append(curPos)
        que.extend([[i[0],i[1]+curLength] for i in river[curPos]])
    return ans

n,m,k,u = map(int,input().rstrip().split())

# a: b,w = length of river
river = [[] for i in range(n+1)]
for i in range(n-1):
    a,b,w = map(int,input().rstrip().split())
    river[a].append([b,w])

# L = init location, S = max swim distance
trouts = [[] for i in range(n+1)]
for i in range(m):
    l,s = map(int,input().rstrip().split())
    trouts[l].append(s)

for i in range(k):
    event = list(map(str,input().rstrip().split()))
    if event[0] == 'Q':
        curPoint = int(event[1])
        print(SearchTrout(curPoint))