from collections import deque
n,m,v = map(int,input().split())
lst = [[] for i in range(n+1)]
for i in range(m):
    for x,y in [list(map(int,input().split()))]:
        lst[x].append(y)
        lst[y].append(x)
for i in lst:
    i.sort()

def go_dfs(cur_node):
    print(cur_node,end=' ')
    
    for i in lst[cur_node]:
        if check[i] == 0:
            check[i] = 1
            go_dfs(i)

def go_bfs(cur_node):
    next=deque()
    next.append(cur_node)
    while next:
        cur = next.popleft()
        print(cur,end=' ')
        for i in lst[cur]:
            if check [i] == 0:
                check[i] = 1
                next.append(i)
                
check = [0]*(n+1)
check[v] = 1
go_dfs(v)
print()
check = [0]*(n+1)
check[v] = 1
go_bfs(v)


#dfs 재귀함수
#bfs for deque