from itertools import combinations_with_replacement

t = int(input())
for _ in range(t):
    m,n = map(int,input().split())
    rowsum = list(map(int,input().split()))
    colsum = list(map(int,input().split()))

    for i in rowsum:
        temp = list(range(i[j]))
        for j in range(len(i)):
            tempcombi = combinations_with_replacement(temp,m)
            for k in range(len(tempcombi)):
                if i[j] == sum(tempcombi[k]):
                    rowsum


    c = int(input())
    for __ in range(c):