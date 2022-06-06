t = int(input())
#안해 이런 더러운 문제
for _ in range(t):
    n,m = map(int,input().split())
    arr = [input() for i in range(n)]
    k = int(input())
    words = [input() for i in range(k)]
    ans = {}
    for i in words:
        ans[i] = [n,m]
    """
    #horizontal
    for i in range(n):
        for j in words:
            if j in arr[i]: 
                if ans[j][0] > i:
                    ans[j] = [i+1, arr[i].index(j)+1]
                elif ans[j][0] == i and arr[i].index(j) < ans[j][1]:
                    ans[j] = [i+1, arr[i].index(j)+1]

    #vertical
    temp = []
    for i in range(m):
        for j in range(n):
            temp.append(arr[j][i])
        for j in words:
            if j in temp:
                if temp.index(j) < ans[j][0]:
                    ans[j] = [arr[i].index(j)+1, i+1]
                elif temp.index(j) == ans[j][0] and i+1 < ans[j][1]:
                    ans[j] = [arr[i].index(j)+1, i+1]
    
    #diagonal \
    vert = [[j for j in i]for i in arr]
    space = [None]*(n-1)
    for i in range(n):
        vert[i] = space[i:] + vert[i] + space[:i]
    hori = [[j for j in i]for i in zip(*vert)]
    for i in range(n):
        for j in words:
            if j in hori[i]:
                if hori[i].index(j) < ans[j][0]:
                    ans[j] = [hori[i].index(j)+1, i+1]
                elif hori[i].index(j) == ans[j][0] and i+1 < i+1-vert[i].count(None):
                    ans[j] = [hori[i].index(j)+1, i+1-vert[i].count(None)]
    """
    #diagonal /
    vert = [[j for j in i]for i in arr]
    space = [None]*(n-1)
    for i in range(n):
        vert[i] = space[:i] + vert[i] + space[i:]
    hori = [[j for j in i]for i in zip(*vert)]

    for i in range(n):
        for j in words:
            if j in hori[i]:
                if hori[i].index(j) < ans[j][0]:
                    ans[j] = [hori[i].index(j)+1, i+1]
                elif hori[i].index(j) == ans[j][0] and i+1 < i+1-vert[i].count(None):
                    ans[j] = [hori[i].index(j)+1, i+1-vert[i].count(None)]