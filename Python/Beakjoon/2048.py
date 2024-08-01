from collections import deque
n = int(input())
arr = [list(map(int,input().split())) for i in range(n)]

def dfs():
    stack = deque()

    while True:
        for i in [[0,0,0,1],[0,0,1,0],[0,n,0,-1],[n,0,-1,0]]: #Down Right Up Left
            