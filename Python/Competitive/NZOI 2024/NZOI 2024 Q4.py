import math
import sys
input = sys.stdin.readline
def dist(cord1,cord2):
    return math.ceil(math.sqrt((cord1[0]-cord2[0])**2 + (cord1[1]-cord2[1])**2))

n,m = map(int,input().rstrip().split())
cities = [list(map(int,input().rstrip().split())) for i in range(n)]
travel = list(map(int,input().rstrip().split()))
totalCost = [0]
for i in range(m-1):
    totalCost.append(totalCost[i] + dist(cities[travel[i]],cities[travel[i+1]]))

for index,i in enumerate(travel):
    ans = 0
    curCost = totalCost[-1]-totalCost[index]
    for j in range(n):
        if j == i:
            continue
        curDist = dist(cities[i],cities[j])
        
        if curDist <= curCost:
            ans+=1
    
    print(ans,end=' ')