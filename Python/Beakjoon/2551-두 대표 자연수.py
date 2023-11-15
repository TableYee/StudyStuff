import math
from statistics import median
#n,*lst = map(int, open(0).read().split())
n = int(input())
lst = list(map(int,input().split()))

print(int(median(lst)), end=' ')
print(math.floor(sum(lst)/n))

"""
minAns, expAns = [10**10,10**10], [10**10,10**10]

for i in range(1,max(lst)+1):
    minSum, expSum = 0,0
    for j in range(n):
        minSum += abs(lst[j] - i)
        expSum += (lst[j] - i)**2

    if minAns[1] > minSum:
        minAns[0], minAns[1] = i, minSum

    if expAns[1] > expSum:
        expAns[0], expAns[1] = i, expSum

print(minAns[0], expAns[0])
"""